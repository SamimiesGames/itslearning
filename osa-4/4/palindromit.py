def palindromi(word):
    return word == word[::-1]


while True:
    palindrome = input("PALINDROME: ")

    if palindromi(palindrome):
        print(f"{palindrome} on palindromi!")
        break
    else:
        print("ei ollut palindromi")
