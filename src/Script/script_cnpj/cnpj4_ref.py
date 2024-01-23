import pandas as pd
import boto3
from os import listdir, scandir
from os.path import isfile, join
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
        s = unidecode(s).replace('@', '_').replace(' ', '_')
        return s[:127]  # Truncate to 127 chars for VARCHAR

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

    def read_and_prepare_data(self, file_path, mapping_folder):
        print(f"Lendo dados de {file_path}...")
        df = pd.read_csv(file_path, dtype=str, low_memory=False, sep=';')
        df.fillna('NULL', inplace=True)

        print("Aplicando mapeamentos...")
        mappings = self.load_mappings(mapping_folder)
        
        varchar_columns = ['numero', 'complemento', 'bairro', 'email','situacao_cadastral', 'identificador_matriz_filial' ]  # Add other VARCHAR columns here
        integer_columns = ['cep', 'ddd_1', 'telefone_1', 'ddd_2', 'telefone_2', 'ddd_fax', 'fax']  # Add other INTEGER columns here
        
        for col in df.columns:
            if col in mappings:
                df[col] = df[col].map(mappings[col]).fillna(df[col])
            if col in varchar_columns:
                df[col] = df[col].apply(lambda x: x[:127])  # Truncate to 127 chars
            if col in integer_columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
        
        print("Limpando texto...")
        for col in varchar_columns:
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
    aws_access_key_id = 'ASIAVOHTC676E4K6DANP'
    aws_secret_access_key = 'ZHgoQvuNhdjLggvNPlL9MDhV43XrJHoMhwyu5iHC'
    aws_session_token = 'IQoJb3JpZ2luX2VjECoaCXVzLWVhc3QtMSJHMEUCICIAeRgOlTMUulYgsSlCUfq3Y+jF3Wa8WxIS9YBzGkpKAiEAlKKzB604OptcHwyREis94rDGYO4AUuHoJ2eWq7NHWHIqoQMIkv//////////ARAAGgwzNzQxNzE5NTcyNDQiDGGPekbxAd3VzgxDWCr1AmTdmZn8hC7Om4f09BU0eA/BuzLJHjpbQcvOLh3hk9u2+rLPQ9HzvexzHs2MsQLZ9p6Hu6k5ghZzE+QVdRW763UrOmxi7jyjbeDMvdZOaMbs8yIM4KcwBtJl+5a+CUcZTol4XXIbXYYVluic0pw8pUJekVSgOjg82dwaTF5PEtkszu1JgdknbeuzhOPdUrrFDEyAlouqnMr3LM0We6shl3TzXAzQ9WK3x0ETh18lEAlyDJV5ArO4IsPQ5SSTkFsnZBH6S3sYCBn6zl/FrVCZcM6jHNfPGR70KiznoICcm0/JepqfvqM+ZDIG4xBEYbTw97DCI5jw9zhXYB6ua9a9w0abeFIs7zETUfYaVEYshwR1u3DwEC5EPiXEshE7qPS2oIHgnn9yuNpKWmtszvI4QioH7uZ2P0Sy00vCh6b+OLYdiXztxBy3F7bH7YuMXyJwrSZ4h6G6x5ch76WvlVeWKzu1+6SJhyy/vMifVot2ZMzqsSVVoWkwtNnCqwY6pgEcLdfvFcVetdq/8OQyqMP9T0HsOjY3CfLT2f/wip+w64qc/q+W1qc8VEmSzr0aCrRHW/AK5vicyx1MzcgjrbcgQB1VYiVNoTvhif75S/58Zfliipbnby5VP6Mqe3lPp3SZEnWdDTr+0UEEIFKdDEx7g7amNY5bK7EugYpSMlJoKw//NlYURiLET1P7miRdcHj02jVUBVwzDxb5RYk1pgd9u6mUmNo/'
    bucket_name = 'bigbytes-cnpj'

    folder_path = '../../dados/dados_cnpj/4'
    s3_folder = 'cnpjs'
    mapping_folder = '../../dicionarios/cnpj'

    if not os.path.isdir(folder_path) or not os.path.isdir(mapping_folder):
        print("Erro: Diretório de dados ou mapeamentos não encontrado.")
        exit()
    
    uploader = S3Uploader(bucket_name, aws_access_key_id, aws_secret_access_key, aws_session_token)
    uploader.upload_folder_to_s3(folder_path, s3_folder, mapping_folder)
    print("Script de upload finalizado.")
