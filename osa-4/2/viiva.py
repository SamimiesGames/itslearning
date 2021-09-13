def viiva(width, string):
    empty_char_fill = "*"  # TMC forces this bad practice.

    is_empty_char = bool(string)

    if is_empty_char:
        first_character = string[0]
        print(first_character * width)
    else:
        print(empty_char_fill * width)


if __name__ == "__main__":
    viiva(5, "")
