import os

def listdir():
    lista_de_diretorios = os.listdir()
    print(lista_de_diretorios)
    return lista_de_diretorios

def retorna_diretorios_e_arquivos(path):

    arquivos = []

    for root, dirs, files in os.walk(path):
        for nome_de_arquivo in files:
            caminho_completo = os.path.join(root, nome_de_arquivo)
            arquivos.append(caminho_completo)
            print(f"Arquivo: {caminho_completo}")

    return arquivos

def verifica_stime():
    ...
            