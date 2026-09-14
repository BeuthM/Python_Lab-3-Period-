import random

def sorter(lst):

    if sum(lst) <= 21:
        print("A soma e menor ou igual a 21")
        return sum(lst)
    elif sum(lst) > 21 and 11 in lst:
        if sum(lst) - 10 <= 21:
            print("A soma e maior que 21 e possui 11")
            return sum(lst) - 10
        else:
            print("A soma excede 21 mesmo apos o reajuste")
            return -1
    else:
        return "Nao encaixou em nenhuma opcao"

print(sorter([random.randint(1,11) for i in range(3)]))