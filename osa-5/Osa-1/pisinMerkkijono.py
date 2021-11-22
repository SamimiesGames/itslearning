def pisin(merkkijonot: list):
    return max(merkkijonot, key=len)


if __name__ == '__main__':
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))
