import boto3

def lambda_handler(event, context):
    # Nome do seu bucket
    bucket_name = 'cnpj5'
    
    # Recupera as chaves de acesso a partir das variáveis de ambiente
    access_key = ''
    secret_key = ''
    
    # Crie uma instância do cliente S3 usando as credenciais associadas ao Lambda
    s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    try:
        # Listar objetos no bucket
        response = s3.list_objects_v2(Bucket=bucket_name)

        # Excluir cada objeto no bucket
        for obj in response.get('Contents', []):
            s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
            print(f"Objeto {obj['Key']} deletado do bucket {bucket_name}")

        # Agora o bucket deve estar vazio, então podemos excluí-lo
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} deletado com sucesso.")
        
        return {
            'statusCode': 200,
            'body': f'Bucket {bucket_name} deletado com sucesso.'
        }
    except Exception as e:
        print(f"Erro ao deletar o bucket {bucket_name}: {str(e)}")
        return {
            'statusCode': 500,
            'body': f'Erro ao deletar o bucket {bucket_name}: {str(e)}'
        }
