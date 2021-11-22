def laske_alkiot(matriisi: list, alkio: int):
    counter = 0
    for i in range(len(matriisi)):
        for j in range(len(matriisi[i])):
            if alkio == matriisi[i][j]:
                counter += 1

    return counter


if __name__ == '__main__':
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))
