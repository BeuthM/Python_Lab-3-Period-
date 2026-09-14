def profit_calc(profit: float, accionists: int) -> float:

    try:

        if int(accionists) <= 0:
            raise ZeroDivisionError("A empresa nao funciona nem acionistas..")

        float(profit)

    except ZeroDivisionError as erro:
        print(f"Erro: {erro}")
        return profit_calc(input("Digite o lucro novamente:\n--> "), input("Digite o numero de acionistas novamente:\n--> "))
    
    except ValueError as erro:
        print(f"Entrada invalida: {erro}")
        return profit_calc(input("Digite o lucro novamente:\n--> "), input("Digite o numero de acionistas novamente:\n--> "))

    else:
        profit = float(profit)
        accionists = int(accionists)

    return profit/accionists

a = input("Digite o lucro: ")
b = input("Digite a quantidade de acionistas na empresa: ")

print(f"Cada acionista rebera: {profit_calc(a, b):.2f}")