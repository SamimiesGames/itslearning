base = [1, 2, 3, 4, 5]

while True:
    index = int(input("INDEX: "))

    if index < 0:
        break

    value = int(input("VALUE: "))

    base[index] = value

    print(base)
