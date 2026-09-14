def num_sorter(n1, n2):
    lst = [n1,n2]

    def verif_even(lst):
        if sum(lst) % 2 != 0:
            return True
        else:
            return False

    if verif_even(lst):
        print(f"O menor numero e: {min(lst)}")
    else:
        print(f"O maior numero e: {max(lst)}")

def verif_type(a, b):
    lst = [a, b]

    try:
        lst = [float(i) for i in lst]
    except:
        print("Entrada invalida")
        return verif_type(input("Digite novamente\n--> ") ,input("--> "))
    else:
        return float(a),float(b)

a = input("Digite o primeiro numero: ")
b = input("Digite o segundo numero: ")

a, b = verif_type(a, b)
num_sorter(a,b)