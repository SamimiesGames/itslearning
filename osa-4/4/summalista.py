def summa(key, value):
    assert len(key) == len(value)

    res = [x + y for x, y in zip(key, value)]

    return res


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(summa(a, b))

