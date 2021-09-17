def parilliset(args: list):
    args = [x for x in args if x % 2 == 0]
    return args


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    uusi_lista = parilliset(lista)
    print("alkuperäinen", lista)
    print("uusi", uusi_lista)
