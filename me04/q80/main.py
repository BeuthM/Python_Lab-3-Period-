# Mise Place (como diria Jackin)

import traceback
import pathlib as pth

pasta = pth.Path(__file__).parent
vendasDB = pasta / "Vendas.txt"
log_Erro = pasta / "Log_Erros.txt"

class ProdutoInvalidoError(Exception):
    def __init__(self, message="O nome do produto nao pode estar vazio"):
        super().__init__(message)
class ValorInvalidoError(Exception):
    def __init__(self, message="O valor do produto tem que estar acima de 0"):
        super().__init__(message)
class QuantidadeInvalidaError(Exception):
    def __init__(self, message="Nao podemos vender quantidades negativas"):
        super().__init__(message)

def registrar_venda(produto: str, preco: str, quantidade: str) -> dict[str, str|float|int]:
    try:
         if len(produto) <= 0:
             raise ProdutoInvalidoError

         if float(preco) <= 0:
             raise ValorInvalidoError

         if int(quantidade) <= 0:
             raise QuantidadeInvalidaError

    except (
        ProdutoInvalidoError,
        ValorInvalidoError,
        QuantidadeInvalidaError,
        TypeError,
        ValueError
    ) as erro:

        print(erro)
        traceback.format_exc()

        with open(log_Erro, "a", encoding="utf-8") as log:
            log.write(f"{traceback.format_exc()}\n")

        return registrar_venda(
            input("Produto: "),
            input("Preco: "),
            input("Quantidade: ")
        )

    else:
        print("Pedido registrado")
        return {
            "produto": produto,
            "preco": float(preco),
            "quantidade": int(quantidade)
            }

    finally:
        print("Processo cncluido")

def gerer_relatorio(vendas: list[list[dict]]):

    if not vendas or all(len(sessao) == 0 for sessao in vendas):
        return {"Aviso": "Nenhum pedido registrado"}

    vendas_produto = {}
    faturamento_total = 0
    total_pedidos = 0

    for i, sessao in enumerate(vendas):
        print(f"sessão {i+1}: ")

        for venda in sessao:
            nome_produto = venda["produto"]
            preco = venda["preco"]
            quantidade = venda["quantidade"]
            
            if nome_produto in vendas_produto:
                vendas_produto[nome_produto] += quantidade
            else:
                vendas_produto[nome_produto] = quantidade

            faturamento_total += preco * quantidade
            total_pedidos += 1

    tickets_medios = sum([len(i) for i in vendas]) / len(vendas)
    mais_vendido = max(vendas_produto, key=vendas_produto.get) 

    return {
        "total de vendas": total_pedidos,
        "mais vendido": mais_vendido,
        "faturamento total": faturamento_total,
        "Media de ticket por venda": tickets_medios
    }

vendas_sec: list[dict] = [] # pedidos desta sessão // vai para o vendas_tot
vendas_tot = [] # todos os pedidos // vai para o .txt

# Interface 

while True:
    produto = input("Digite o nome do produto: ")

    if produto.lower() == "fim":
        print("Entendido, terminando programa")
        break

    preco = input("Digite o preco do produto: ")
    quantidade = input("Digite a quantidade a ser vendida: ")

    vendas_sec.append(registrar_venda(produto, preco, quantidade))

vendas_tot.append(vendas_sec)

with open(vendasDB, "a", encoding="utf-8") as log:
    log.write(f"{str(vendas_tot)}\n")

print("Dados salvos, gerando o relatório...")

for k, v in gerer_relatorio(vendas_tot).items():
    print(f"{k}: {v}")