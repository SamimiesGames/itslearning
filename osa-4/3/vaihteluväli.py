def vaihteluvali(args):
    return max(args) - min(args)


if __name__ == '__main__':
    lista = [3, 6, -4]
    tulos = vaihteluvali(lista)
    print(tulos)
