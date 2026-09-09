matriz = [
    [1,0,1],
    [1,1,0],
    [0,1,1]
]

ocupadas = 0
livres = 0

for i in matriz:
    for j in matriz[i]:
        if matriz[i][j] == 0:
            livres += 1
        else:
            ocupadas += 1


print(f"Cadeiras ocupadas {ocupadas}")
print(f"Cadeiras livres {livres}")