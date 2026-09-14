lst = ["python2023" , "0203programacao2023", "luz azul", "arara rara", "anotaram a data da maratona"]

def str_invert(lista: list[str]) -> list[str]:

    for item in range(len(lista)):

        if " " in lista[item]:
            item_words = lista[item].split()

            for word in range(len(item_words)):
                if len(item_words[word]) > 0:
                    item_words[word] = list(item_words[word])[::-1]
                    item_words[word] = "".join(item_words[word])
                else:
                    continue

            lista[item] = " ".join(item_words[::-1])

        else:
            lista[item] = list(lista[item])[::-1]
            lista[item] = "".join(lista[item])

    for i, e in enumerate(lista):
        print(f"{i+1}. {e}")

str_invert(lst)