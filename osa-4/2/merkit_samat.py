def samat(string, first, second):
    i_len = len(string) - 1

    if first <= i_len and second <= i_len:
        return string[first] == string[second]
    else:
        return False


if __name__ == '__main__':
    print(samat("koodi", 1, 1))
