def temp_converter(f):
    return (5/9) * (f - 32)

def verif_type(f):

    try:
        float(f)
    except:
        print("Entrada invalida!!")
        return verif_type(input("Digite novamente:\n--> "))
    else:
        return float(f)

f = verif_type(input("Digite 1 numero:\n--> "))

print(f"{temp_converter(f):.2f}C°")