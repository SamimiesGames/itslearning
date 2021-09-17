def pisimmat(array):
    max_values = []
    _max_value = 0

    while True:
        max_item = max(array, key=len)
        max_value = len(max_item)

        if max_value < _max_value:
            break

        _max_value = max_value
        max_values.append(max_item)
        array.remove(max_item)

    return max_values


if __name__ == '__main__':
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]

    tulos = pisimmat(lista)
    print(tulos)
