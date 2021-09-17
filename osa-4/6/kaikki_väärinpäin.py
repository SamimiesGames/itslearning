def kaikki_vaarinpain(array):
    return [x[::-1] for x in array][::-1]


if __name__ == '__main__':
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)
