# cant declare import from viiva because TMC doesn't support my ".idea" environment.


def viiva(width, string):
    empty_char_fill = "*"  # TMC forces this bad practice.

    is_empty_char = bool(string)

    if is_empty_char:
        first_character = string[0]
        print(first_character * width)
    else:
        print(empty_char_fill * width)


def kolmio(size, string):
    for index in range(size):
        width = index + 1

        viiva(width, string)


def nelio(height, width, character):
    for y in range(height):
        viiva(width, character)


def kuvio(width, header, height, footer):
    kolmio(width, header)
    nelio(height, width, footer)


if __name__ == '__main__':
    kuvio(3, "o", 5, "x")
