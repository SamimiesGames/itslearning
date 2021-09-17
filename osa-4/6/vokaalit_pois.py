def ilman_vokaaleja(string):
    vowels = "aeiouyäöå"  # TMC doesn't allow constant global variables

    for vowel in vowels:
        string = string.replace(vowel, "")

    return string


if __name__ == '__main__':
    print(ilman_vokaaleja("tämä on esimerkki"))
