registro = {}

while True:
    act = input("Acao ['registrar' ou 'sair']: ")
    if act.lower().strip() in ["registrar", 'sair']:
        if act == 'sair':
            break
    
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    registro[nome] = nota

    if nota >= 7:
        alunos_up += 1

media_turma = sum(registro.values()) / len(registro)
alunos_up = 0

print("Alunos Aprovados")
for k, v in registro.items():
    if v >= 7:
        print(f'Aluno: {k}\n\tNota: {v}')
        alunos_up += 1

print(f"Média da turma: {media_turma}")
print(f"Relação Aprovados/Turma: {alunos_up/len(registro)}")