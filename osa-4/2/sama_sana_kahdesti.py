words = []


while True:
    word = input("WORD: ")

    if word in words:
        break

    words.append(word)


print(f"Annoit {len(words)} eri sanaa.")
