from src.main import retorna_path_de_arquivos, calcula_stime, converte_timestamp_para_datetime
import datetime

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

def test_converte_timestamp_para_datetime():

    data_convertida = converte_timestamp_para_datetime(1.0)

    data_correta_timestamp = datetime.datetime(year=1969, month=12, day=31, hour=21, minute=0,second=1)

    assert isinstance(data_convertida, datetime.datetime)
    assert data_convertida == data_correta_timestamp
    