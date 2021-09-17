def muotoile(array):
    return [f"{x:.2f}" for x in array]


if __name__ == '__main__':
    lista = [1.234, 0.3333, 0.11111, 3.446]
    lista2 = muotoile(lista)
    print(lista2)
