def calculaCubo(n: float) -> float:
    print("calculando o cubo...")
    return n**3

def calcularDivisaoCubo(n: float) -> float | bool:
    print("Verificando se pode calcular o cubo...")
    if n % 3 == 0:
        return calculaCubo(n)
    else:
        return False

print(calculaCubo(float(input("Digite um valor\n--> "))))
print(calcularDivisaoCubo(float(input("Digite outro valor:\n--> "))))