def pisimman_pituus(array):
    value = max(array, key=len)
    return len(value)


if __name__ == '__main__':
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]

    tulos = pisimman_pituus(lista)
    print(tulos)
