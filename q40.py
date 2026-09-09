import random

sort_num = random.randint(-999999999,999999999)
user_num = int(input("Numero: "))

if user_num > sort_num:
    print("O numero e menor que o que voce escolheu!!")
elif user_num < sort_num:
    print("O numero e maior que o que voce escolheu!!")
else:
    print("Acertou!!")