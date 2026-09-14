import pathlib as pth

def verif_file(file: str):
    arquivo = pth.Path(file)

    try:
        if not arquivo.exists():
            raise FileNotFoundError("Arquivo nao encontrado...")
    except FileNotFoundError as erro:
        print(f"Erro: {erro}")
    finally:
        print("Encerrando programa")

verif_file("relatorio_vendas.txt")