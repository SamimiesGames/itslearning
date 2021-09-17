def positiivisten_summa(args):
    args = [x for x in args if x > 0]
    return sum(args)


if __name__ == '__main__':
    lista = [1, -2, 3, -4, 5]
    vastaus = positiivisten_summa(lista)
    print("vastaus", vastaus)
