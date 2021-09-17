def eniten_kirjainta(string):
    array = [x for x in string]
    char = max(array, key=array.count)

    return char


if __name__ == '__main__':
    mjono = "abcbdbe"
    print(eniten_kirjainta(mjono))

    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))
