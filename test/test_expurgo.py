from src.main import listdir, retorna_diretorios_e_arquivos


def test_listdir():
    list_dire = listdir()

    assert list_dire
    assert isinstance(list_dire, list)

def test_retorna_diretorios_e_arquivos():
    retorna_diretorios_e_arquivos(".")
    