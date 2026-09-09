total = 0

while True:
    value = input("Valor [Digite '0' para sair]: ")

    try:
        int(float(value))
    except:
        continue

    if value == "0":
        print(f"A soma das notas foi {total}")
        break

    total += float(value)