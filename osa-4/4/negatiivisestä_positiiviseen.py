number = int(input("NUMBER: "))

for i in range((number * 2) + 1):
    value = i - number

    if value == 0:
        continue

    print(value)

