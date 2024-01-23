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
        s = str(s)  # Converte o valor em string
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
        
        # Diagnóstico para coluna específica V9016
        if 'V9016' in mappings:
            print(f"Mapping para 'V9016' carregado com sucesso.")
        else:
            print(f"AVISO: Mapping para 'V9016' não encontrado.")
        
        return mappings

    def read_and_prepare_data(self, file_path, mapping_folder):
        print(f"Lendo dados de {file_path}...")
        df = pd.read_csv(file_path, dtype=str, low_memory=False)
        df.fillna(0, inplace=True)

        print("Aplicando mapeamentos...")
        mappings = self.load_mappings(mapping_folder)
        binary_mappings = {
            'V9019': {1: 'sim', 0: 'nao'},
            'V9020': {1: 'sim', 0: 'nao'},
            'V9021': {1: 'sim', 0: 'nao'},
            'V9022': {1: 'sim', 0: 'nao'},
            'V9023': {1: 'sim', 0: 'nao'},
            'V9024': {1: 'sim', 0: 'nao'},
            'V9025': {1: 'sim', 0: 'nao'},
            'V9026': {1: 'sim', 0: 'nao'},
            'V9027': {1: 'sim', 0: 'nao'},
            'V9028': {1: 'sim', 0: 'nao'},
            'V9029': {1: 'sim', 0: 'nao'},
            'V9030': {1: 'sim', 0: 'nao'},
            'DIA_ATIPICO': {1: 'sim', 0: 'nao'}
        }

        for col in df.columns:
            if col in mappings:
                df[col] = df[col].map(mappings[col]).fillna(0)
            elif col in binary_mappings:
                df[col] = pd.to_numeric(df[col], errors='coerce').map(binary_mappings[col]).fillna(0)

        if 'V9016' in df.columns:
            print("Amostra da coluna 'V9016' após mapeamento:")
            print(df['V9016'])

        print("Limpando texto...")
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].apply(self.clean_text)

        return df

    def upload_file(self, file_path, s3_path, mapping_folder):
        df = self.read_and_prepare_data(file_path, mapping_folder)
        print("Dados processados:")
        print(df.head())

        csv_buffer = StringIO()
        df.to_csv(csv_buffer, sep=',', index=False, encoding='utf-8')
        self.s3.put_object(Bucket=self.bucket_name, Key=s3_path, Body=csv_buffer.getvalue())
        print(f"Uploaded {file_path} to S3 bucket {self.bucket_name} at {s3_path}")

    def upload_folder_to_s3(self, folder_path, s3_folder, mapping_folder):
        print(f"Processando pasta: {folder_path}")
        for entry in scandir(folder_path):
            if entry.is_file() and entry.name.endswith('.csv'):
                self.upload_file(entry.path, f"{s3_folder}/{entry.name}", mapping_folder)

if __name__ == "__main__":
    aws_access_key_id = ''
    aws_secret_access_key = ''
    aws_session_token = ''
    bucket_name = 'bigbytes-pof'

    folder_path = '../../dados/dados_pof/consumo_alimentar'
    s3_folder = 'pof'
    mapping_folder = '../../dicionarios/consumo_alimentar_pof'

    if not os.path.isdir(folder_path) or not os.path.isdir(mapping_folder):
        print("Erro: Diretório de dados ou mapeamentos não encontrado.")
        exit()

    uploader = S3Uploader(bucket_name, aws_access_key_id, aws_secret_access_key, aws_session_token)
    uploader.upload_folder_to_s3(folder_path, s3_folder, mapping_folder)
    print("Script de upload finalizado.")
