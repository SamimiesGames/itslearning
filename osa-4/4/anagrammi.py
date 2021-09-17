def anagrammi(key, value):
    value = [x for x in value]

    if len(key) != len(value):
        return False

    for letter in key:
        if letter not in value:
            return False

        value.remove(letter)

    return True


if __name__ == '__main__':
    print(anagrammi("testi", "setsi"))
