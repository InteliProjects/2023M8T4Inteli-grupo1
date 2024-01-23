import requests
import json
import pprint
import boto3
from botocore.exceptions import NoCredentialsError
from unidecode import unidecode
import string

def preprocessar_dados(dados):
    dados_processados = {}
    for nome_tabela, dados_tabela in dados.items():

        nome_tabela_limpo = unidecode(nome_tabela)
        

        nome_tabela_limpo = ''.join(char for char in nome_tabela_limpo if char.isalnum())


        dados_tabela_limpos = {}
        for nome_coluna, valores_coluna in dados_tabela.items():
            nome_coluna_limpo = unidecode(nome_coluna)
            nome_coluna_limpo = ''.join(char for char in nome_coluna_limpo if char.isalnum())

            valores_limpos = [unidecode(str(valor)) for valor in valores_coluna]
            dados_tabela_limpos[nome_coluna_limpo] = valores_limpos

        dados_processados[nome_tabela_limpo] = dados_tabela_limpos

    return dados_processados


def fazer_upload_no_s3(dados, nome_tabela):
    s3 = boto3.client('s3', aws_access_key_id='SUA_CHAVE_DE_ACESSO',
                      aws_secret_access_key='SEU_SEGREDO')
    nome_bucket = 'seu-nome-de-bucket-s3'
    nome_arquivo = f"{nome_tabela}.json"

    try:
        
        dados_json = json.dumps(dados, indent=2)

        
        s3.put_object(Body=dados_json, Bucket=nome_bucket, Key=nome_arquivo)
        print(f"Dados para {nome_tabela} enviados com sucesso para o S3.")
    except NoCredentialsError:
        print("Credenciais não disponíveis.")

url = "https://intelifunctiongetdata.azurewebsites.net/api/InteliFunctionGetData"
parametros = {
    "code": "",
    "tables": ["Sale", "Establishment", "Category"],
}

resposta = requests.get(url, params=parametros)

if resposta.status_code == 200:
    dados = resposta.json()
    pprint.pprint(dados)

    
    dados_processados = preprocessar_dados(dados)

    for nome_tabela, dados_tabela in dados_processados.items():
        
        fazer_upload_no_s3(dados_tabela, nome_tabela)
else:
    print("Falha ao obter os dados. Código de status:", resposta.status_code)
