lst = {}
for i in range(5):
    lst[input("Nome do produto: ")] = float(input("Preco: "))

query = input("Qual item você deseja buscar: ")

if query in lst:
    print(f"{query}: R$ {lst[query]}")
else:
    print("Item não encontrado...")