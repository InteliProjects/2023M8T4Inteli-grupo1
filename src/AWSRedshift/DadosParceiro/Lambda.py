import luigi
import requests
import redshift_connector
from datetime import datetime, timedelta
import time
from unidecode import unidecode
import csv
import xml.etree.ElementTree as ET

class ExtractFromAPI(luigi.Task):
    def output(self):
        return luigi.LocalTarget('data_api.txt')

    def run(self):
        url = "https://intelifunctiongetdata.azurewebsites.net/api/InteliFunctionGetData"
        bases = ["Sale", "Establishment", "Category"]

        for base in bases:
            params = {
                "code": "",
                "table": base,
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                with self.output().open('a') as f:
                    for record in data:
                        timestamp = int(time.time())
                        record["timestamp"] = timestamp
                        f.write(str(record) + '\n')

class ExtractFromCSV(luigi.Task):
    def output(self):
        return luigi.LocalTarget('data_csv.txt')

    def run(self):
        csv_path = "path/to/your/file.csv"
        with open(csv_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            with self.output().open('w') as out_file:
                for row in csv_reader:
                    out_file.write(','.join(row) + '\n')

class ExtractFromTXT(luigi.Task):
    def output(self):
        return luigi.LocalTarget('data_txt.txt')

    def run(self):
        txt_path = "path/to/your/file.txt"
        with open(txt_path, 'r') as txt_file:
            with self.output().open('w') as out_file:
                for line in txt_file:
                    out_file.write(line)

class LoadToRedshift(luigi.Task):
    def requires(self):
        return {
            'api': ExtractFromAPI(),
            'csv': ExtractFromCSV(),
            'txt': ExtractFromTXT(),
        }

    def run(self):
        connection_params = {
            'host': '',
            'database': '',
            'user': '',
            'password': '',
            'port': '',
        }
        connection = None
        cursor = None

        try:
            connection = redshift_connector.connect(**connection_params)
            cursor = connection.cursor()

            for task_name, input_target in self.input().items():
                with input_target.open('r') as f:
                    if task_name == 'csv':
                        reader = csv.DictReader(f)
                    else:
                        reader = f.readlines()

                    for line in reader:
                        if isinstance(line, dict):  # Se é um dicionário (CSV)
                            record = {key: tirar_acentos_espacos(str(value)) for key, value in line.items()}
                        else:  # Se é uma linha de texto (TXT)
                            # Adapte esta lógica conforme necessário
                            columns = line.strip().split('|')
                            record = {f'column_{i}': tirar_acentos_espacos(str(value)) for i, value in enumerate(columns)}

                        table_name = 'APIdb'
                        columns = record.keys()
                        values = tuple(record.values())
                        insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"
                        cursor.execute(insert_query, values)

            connection.commit()

        except Exception as e:
            print("Error inserting data into Redshift:", e)

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

def tirar_acentos_espacos(texto):
    texto_sem_acentos = unidecode(texto)
    texto_sem_acentos = texto_sem_acentos.replace(" ", "_")  # Substitui espaços por underscores, por exemplo
    return texto_sem_acentos

class VerificarMudancasDiarias(luigi.Task):
    def output(self):
        return luigi.LocalTarget('status.txt')

    def run(self):
        data_atual = datetime.now().strftime('%Y-%m-%d')
        mudancas_detectadas = self.detectar_mudancas()

        with self.output().open('w') as f:
            f.write(f'{data_atual}\nMudanças detectadas: {mudancas_detectadas}')

        if mudancas_detectadas:
            self.ativar_etl()

    def detectar_mudancas(self):
        bases = ["Sale", "Establishment", "Category"]
        mudancas_detectadas = False

        for base in bases:
            ids_atual = self.obter_ids_atuais(base)
            ids_anteriores = self.obter_ids_anteriores(base)

            if set(ids_atual) != set(ids_anteriores):
                mudancas_detectadas = True
                break

        return mudancas_detectadas

    def obter_ids_atuais(self, base):
        url = f"https://intelifunctiongetdata.azurewebsites.net/api/InteliFunctionGetData?code=&table={base}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            ids_atuais = [record.get("id") for record in data]
            return ids_atuais
        else:
            print(f"Erro ao obter IDs atuais para a base {base}. Código de status: {response.status_code}")
            return []

    def obter_ids_anteriores(self, base):
        arquivo_ids = f'ids_anteriores_{base}.txt'
        try:
            with open(arquivo_ids, 'r') as f:
                ids_anteriores = [int(line.strip()) for line in f.readlines()]
        except FileNotFoundError:
            ids_anteriores = []
        return ids_anteriores

    def ativar_etl(self):
        etl_task = LoadToRedshift()
        luigi.build([etl_task], local_scheduler=True)

if __name__ == "__main__":
    luigi.build([VerificarMudancasDiarias()], local_scheduler=True)

        