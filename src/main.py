import os
from datetime import datetime


# def listdir():
#     lista_de_diretorios = os.listdir()
#     print(lista_de_diretorios)
#     return lista_de_diretorios

def retorna_path_de_arquivos(path):

    arquivos_paths = []

    for root, dirs, files in os.walk(path):
        for nome_de_arquivo in files:
            caminho_completo = os.path.join(root, nome_de_arquivo)
            arquivos_paths.append(caminho_completo)
            print(f"Arquivo: {caminho_completo}")

    return arquivos_paths

def calcula_stime(path):
    for file in path:        
        print(f"file: {file} stime: {os.stat(file).st_atime} datetime {converte_timestamp_para_datetime(os.stat(file).st_atime)}")
    ...

def converte_timestamp_para_datetime(timestamp):

    data_convertida = datetime.fromtimestamp(timestamp)

    return data_convertida

def calcula_diferença_de_dias(data_calculo, data_base=datetime.now()):
    diferenca_de_tempo = data_calculo - data_base
    diferenca_de_dias = diferenca_de_tempo.days

    return diferenca_de_dias



    
            