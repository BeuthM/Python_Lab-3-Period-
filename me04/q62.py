def perfect_num(n: int) -> bool:

    divs = [i for i in range(1, n) if n % i == 0]

    if sum(divs) == n:
        return True
    else:
        return False

print(perfect_num(int(input("Digite um numero:\n--> "))))