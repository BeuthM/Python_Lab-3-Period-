MATERIAS = ("Portugues","Matematica")
registro = {}

while True:

    nome = input("Nome: ")
    if not nome:
        break
    nota_p = float(input("Nota de portugues: "))
    nota_m = float(input("Nota de matematica: "))
    media = nota_p+nota_m/len(MATERIAS)


    registro[nome] = {
        MATERIAS[0]: nota_p,
        MATERIAS[1]: nota_m,
        "media": media,
        "status":"aprovado" if media >= 7 else "reprovado"
    }

print(f"matérias:\n\t{MATERIAS[0]}\n\t{MATERIAS[1]}")

for n, s in registro.items():
    print(f"{n}:")
    for k, v in registro[n].items():
        print(f"\t{k} --- {v}")