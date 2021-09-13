# cant declare import from viiva because TMC doesn't support my ".idea" environment.


def viiva(width, string):
    empty_char_fill = "*"  # TMC forces this bad practice.

    is_empty_char = bool(string)

    if is_empty_char:
        first_character = string[0]
        print(first_character * width)
    else:
        print(empty_char_fill * width)


def kuvio(header_size, header, footer_size, footer):
    ...


if __name__ == '__main__':
    kuvio("o", 3, "x", 5)
