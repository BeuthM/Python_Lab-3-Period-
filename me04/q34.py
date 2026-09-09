registro = {}
num_student = int(input("Numero de estudantes: "))

for i in range(num_student):
    nome = input("Nome do aluno: ")
    nota = float(input("Nota: "))
    registro[nome] = nota

query = input("Nome do aluno que deseja verificar: ")
if query in registro:
    print(registro[query])
else:
    print("O nome nao encontrado")