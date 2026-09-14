def conversor(n: str) -> int:

    try:
        if int(n) <= 0:
            raise ValueError
    except ValueError as erro:
        print(f"Entrada invalida: {erro}")
        return None
    else:
        return int(n)
    
while True:
    in_age = input("Digite sua idade: ")

    if isinstance(conversor(in_age), int):
        print("Idade convertida")
        break
    else:
        print("Tente novamente")