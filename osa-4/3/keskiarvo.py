def keskiarvo(args):
    return sum(args) / len(args)


if __name__ == "__main__":
    lista = [3, 6, -4]
    tulos = keskiarvo(lista)
    print(tulos)
