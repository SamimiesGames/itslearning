def uniikit(array):
    uniques = []
    for value in sorted(array):
        if value not in uniques:
            uniques.append(value)

    return uniques


if __name__ == '__main__':
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista))
