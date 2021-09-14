# Kirjoita ratkaisu tähän
num = int(input("Anna luku: "))

i = 0

if num % 2 == 0:
    while i < num / 2:
        print(i+1)
        print(num - i)
        i += 1
else:
    while i < (num - 1) / 2:
        print(i+1)
        print(num - i)
        i += 1
    print(i + 1)