import requests

def try_connect(endpoint, time=1):

    try:
        resposta = requests.get(f"https://SiteFicticio.com/api/produto/{endpoint}")
    except requests.exceptions.ConnectionError:
        if time > 3:
            return "ERRO: Falha ao se conectar"
        else:
            print(f"Tentando se conectar ({time} vez)")
            return try_connect(endpoint, time+1)
    except Exception:
        return "Erro inesperado"

print(try_connect("banana"))