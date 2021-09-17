def poista_isot(array):
    return [x for x in array if not x.isupper()]


if __name__ == '__main__':
    lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)
