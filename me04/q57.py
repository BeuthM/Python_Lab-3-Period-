def char_counter(string, char):

    try:
        if len(char.strip()) != 1 :
            raise TypeError("Charactere invalido")
    except TypeError as erro:
            print(f"Erro: {erro}")
            return char_counter(string,input("Digite novamente: "))
        
    n = 0
    for i in string:
        if i == char:
            n += 1

    return n

print(char_counter("banana","ana"))