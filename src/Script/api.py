import boto3
import pandas as pd
import requests
from io import StringIO
from unidecode import unidecode
import pprint

class DataHandler:
    def __init__(self, aws_access_key_id, aws_secret_access_key, aws_session_token, bucket_name):
        self.uploader = S3Uploader(bucket_name, aws_access_key_id, aws_secret_access_key, aws_session_token)

    def fetch_data(self, table):
        url = "https://intelifunctiongetdata.azurewebsites.net/api/InteliFunctionGetData"
        params = {
            "code": "",
            "table": table,
        }
        response = requests.get(url, params=params)
        return response

    def clean_data(self, response):
        resposta = response.json()
        if not isinstance(resposta, list):
            print("Erro: A resposta da API não é uma lista.")
            return {}

        dados_tabela_limpos = []
        for registro in resposta:
            registro_limpo = {}
            for nome_coluna, valor in registro.items():
                nome_coluna_limpo = unidecode(nome_coluna)
                nome_coluna_limpo = ''.join(char for char in nome_coluna_limpo if char.isalnum())
                valor_limpo = unidecode(str(valor))
                registro_limpo[nome_coluna_limpo] = valor_limpo
            dados_tabela_limpos.append(registro_limpo)

        return dados_tabela_limpos

    def process_and_upload(self, table):
        response = self.fetch_data(table)
        if response.status_code == 200:
            pprint.pprint(response.json())
            cleaned_data = self.clean_data(response)
            s3_path = f'integrationcliente/{table.lower()}_data.json'
            self.uploader.upload_data(cleaned_data, s3_path)
        else:
            print(f"Failed to obtain data for the table {table}. Status code: {response.status_code}")

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

    def upload_data(self, data, s3_path):
        df = pd.DataFrame(data)  # Convert JSON data to a pandas DataFrame
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        self.s3.put_object(Bucket=self.bucket_name, Key=s3_path, Body=csv_buffer.getvalue())
        print(f"Uploaded data to S3 bucket {self.bucket_name} at {s3_path}")

if __name__ == "__main__":
    aws_access_key_id = ''
    aws_secret_access_key = ''
    aws_session_token = ''
    bucket_name = 'bigbytes-integration'
    tables = ["Sale", "Category", "Establishment"]

    data_handler = DataHandler(aws_access_key_id, aws_secret_access_key, aws_session_token, bucket_name)
    
    for table in tables:
        data_handler.process_and_upload(table)
