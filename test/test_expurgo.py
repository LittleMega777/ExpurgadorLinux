from src.main import listdir, retorna_path_de_arquivos, calcula_stime


path_raiz = "."

# def test_listdir():
#     list_dire = listdir()

#     assert list_dire
#     assert isinstance(list_dire, list)

def test_retorna_diretorios_e_arquivos():
    lista_de_arquivos = retorna_path_de_arquivos(path_raiz)

    assert isinstance(lista_de_arquivos, list)

def test_verifica_stime():
    lista_de_arquivos = retorna_path_de_arquivos(path_raiz)

    calcula_stime(lista_de_arquivos)
    ...
    