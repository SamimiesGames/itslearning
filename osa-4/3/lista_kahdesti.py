numbers = []

while True:
    number = int(input("NUMBER: "))

    if number <= 0:
        break

    numbers.append(number)

    print("Lista:", numbers)
    print("Järjestettynä:", sorted(numbers))


print("Moi!")
