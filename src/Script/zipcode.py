import pandas as pd
import boto3
from os import listdir, scandir
from os.path import isfile, join, isdir
from io import StringIO
import os
from unidecode import unidecode

class S3Uploader:
    def __init__(self, bucket_name, aws_access_key_id, aws_secret_access_key, aws_session_token):
        self.s3 = boto3.client(
            's3',
            region_name='us-east-1',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token
        )
        self.bucket_name = bucket_name

    def clean_text(self, s):
        if isinstance(s, str):
            s = unidecode(s)
            s = s.replace('@', '_').replace(' ', '_')
        return s

    def load_mappings(self, mapping_folder):
        print("Carregando mapeamentos...")
        mappings = {}
        for file_name in listdir(mapping_folder):
            if file_name.endswith('.csv'):
                column_name = file_name[:-4]
                path = join(mapping_folder, file_name)
                df_mapping = pd.read_csv(path, dtype={'codigo': str, 'descricao': str})
                mappings[column_name] = df_mapping.set_index('codigo')['descricao'].to_dict()
        return mappings

    def read_and_prepare_data(self, df, mapping_folder):
        print("Aplicando mapeamentos...")
        mappings = self.load_mappings(mapping_folder)
        for col in df.columns:
            if col in mappings:
                df[col] = df[col].map(mappings[col]).fillna('Unknown')

        print("Limpando texto...")
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].apply(self.clean_text)

        return df

    def concatenate_state_data(self, folder_path):
        state_dfs = {}
        for entry in scandir(folder_path):
            if entry.is_dir():
                state_code = entry.name  # O nome da pasta é o código do estado
                state_folder_path = join(folder_path, state_code)
                dfs = [pd.read_csv(join(state_folder_path, f), dtype=str) for f in listdir(state_folder_path) if f.endswith('.csv')]
                state_dfs[state_code] = pd.concat(dfs, ignore_index=True)
        return state_dfs

    def process_and_upload_data(self, folder_path, mapping_folder, s3_folder):
        state_dfs = self.concatenate_state_data(folder_path)
        for state_code, df in state_dfs.items():
            df = self.read_and_prepare_data(df, mapping_folder)  # Aplica mapeamentos e limpeza
            s3_path = f"{s3_folder}/{state_code}.csv"
            csv_buffer = StringIO()
            df.to_csv(csv_buffer, sep=',', index=False, encoding='utf-8')
            self.s3.put_object(Bucket=self.bucket_name, Key=s3_path, Body=csv_buffer.getvalue())
            print(f"Uploaded {state_code} data to S3 bucket {self.bucket_name} at {s3_path}")

if __name__ == "__main__":
    aws_access_key_id = ''
    aws_secret_access_key = ''
    aws_session_token = ''
    bucket_name = 'bigbytes-cep'

    folder_path = '../dados/CEP'
    s3_folder = 'cep'
    mapping_folder = '../dicionarios/cep'

    if not os.path.isdir(folder_path) or not os.path.isdir(mapping_folder):
        print("Erro: Diretório de dados ou mapeamentos não encontrado.")
        exit()

    uploader = S3Uploader(bucket_name, aws_access_key_id, aws_secret_access_key, aws_session_token)
    uploader.process_and_upload_data(folder_path, mapping_folder, s3_folder)
    print("Script de upload finalizado.")
