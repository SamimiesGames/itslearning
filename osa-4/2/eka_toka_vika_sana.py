def eka_sana(words):
    return words.split(" ")[0]


def toka_sana(words):
    return words.split(" ")[1]


def vika_sana(words):
    return words.split(" ")[-1]


if __name__ == "__main__":
    lause = "olipa kerran kauan sitten ohjelmoija"
    print(eka_sana(lause))
    print(toka_sana(lause))
    print(vika_sana(lause))

