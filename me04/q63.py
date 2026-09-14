def min_max(n: list[float]) -> list[float]:

    def maximus(n):
        return max(n)

    def minus(n):
        return min(n)

    return f"Maximo: {maximus(n)}\nMinimo: {minus(n)}"

lst = [int(input("Digite um numero: ")) for i in range(5)]

print(min_max(lst))