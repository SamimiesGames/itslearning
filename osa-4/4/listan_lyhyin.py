def lyhin(array):
    return min(array, key=len)


if __name__ == '__main__':
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]

    tulos = lyhin(lista)
    print(tulos)
