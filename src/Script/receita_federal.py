import boto3
import pandas as pd
from os import listdir
from os.path import isfile, join
from io import StringIO

class S3Uploader:
    def __init__(self, bucket_name, aws_access_key_id, aws_secret_access_key):
        self.s3 = boto3.client(
            's3',
            region_name='us-east-1',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        self.bucket_name = bucket_name

    def read_and_prepare_data(self, file_path):
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path, encoding='ISO-8859-1', sep=';')
        elif file_path.endswith('.json'):
            df = pd.read_json(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format")
        
        df.fillna(0, inplace=True)
        return df

    def upload_file(self, file_path, s3_path):
        df = self.read_and_prepare_data(file_path)
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)  # Adicione index=False aqui
        self.s3.put_object(Bucket=self.bucket_name, Key=s3_path, Body=csv_buffer.getvalue())
        print(f"Uploaded {file_path} to S3 bucket {self.bucket_name} at {s3_path}")

    def upload_folder_to_s3(self, folder_path, s3_folder):
        files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
        for file_name in files:
            if file_name.endswith('.csv'):
                file_path = join(folder_path, file_name)
                s3_path = f"{s3_folder}/{file_name}"
                self.upload_file(file_path, s3_path)
        
    # def upload_file_to_azure(self, file_path, container_name, blob_name):
    #     blob_service_client = BlobServiceClient.from_connection_string(self.azure_connection_string)
    #     container_client = blob_service_client.get_container_client(container_name)
    #     try:
    #         container_client.create_container()
    #     except Exception as e:
    #         print(f"Container já existe ou ocorreu um erro: {e}")
    #     with open(file_path, 'rb') as data:
    #         blob_client = container_client.get_blob_client(blob_name)
    #         blob_client.upload_blob(data, overwrite=True)
    #         print(f"Uploaded {file_path} to Azure blob storage container {container_name} as blob {blob_name}")


if __name__ == "__main__":
    aws_access_key_id = 'AKIATMJ74GQSJ4Q2IYAY'
    aws_secret_access_key = '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'
    bucket_name = 'receita-federal-bigbytes'
    folder_path = '../dados/receita_federal' 
    s3_folder = 'receita_federal'
    # azure_connection_string = 'your_azure_connection_string'
    # azure_container_name = 'your_azure_container_name'

    uploader = S3Uploader(bucket_name, aws_access_key_id, aws_secret_access_key)
    uploader.upload_folder_to_s3(folder_path, s3_folder)

    # for file_name in listdir(folder_path):
    #     if file_name.endswith('.csv'):
    #         file_path = join(folder_path, file_name)
    #         blob_name = f"{s3_folder}/{file_name}"
    #         uploader.upload_file_to_azure(file_path, azure_container_name, blob_name)
