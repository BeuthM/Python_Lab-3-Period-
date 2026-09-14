data = {
    "Matheus": {
        "password": "13@Ghz76",
        "email": "mat@mail.com",
        "permission": "staff"
    },
    "Silva": {
        "password": "%Ij28m43",
        "email": "sil@mail.com",
        "permission": "admin"
    },
    "Joao": {
        "password": "13@Ghz76",
        "email": "joa@mail.com",
        "permission": "user"
    },
    "Alice": {
        "password": "32F%kjb2",
        "email": "ali@mail.com",
        "permission": None
    }
}

perms = ["admin", "staff", "user"]

def perm_verif(name: str, index: int) -> str:

    try:
        x = data[name]
        y = perms[int(index)]

    except KeyError as erro:
        print(f"ERRO: {erro} (Nome nao encontrado)")
        return perm_verif(input("Digite o nome novamente: "), index)

    except IndexError as erro:
        print(f"ERRO: {erro} (Codigo de permissao nao encontrado)")
        return perm_verif(name, input("Digite o codigo novamente: "))

    except ValueError as erro:
        print(f"ERRO: {erro} (Digite um numero no campo de codigo)")
        return perm_verif(name, input("Digite o nome novamente: "))

    if data[name]["permission"] == perms[int(index)]:
        return perms[int(index)]
    else:
        return "acesso_restrito"
        
print(perm_verif("Matheus", "1"))
print(perm_verif("Silva", "0"))
print(perm_verif("Joao", "2"))
print(perm_verif("Alice", "0"))
print(perm_verif("Josimar", "4"))