lst = []
for i in range(5):
    temp = float(input("Temperatura: "))
    lst.append(temp)

media = sum(lst)/len(lst)
print(f"A media e: {media}")

if 18 < media < 28:
    print("Temperatura Ideal!!")
else:
    print("Temperatura desfavoravel!!")

print(lst)