# cant declare import from viiva because TMC doesn't support my ".idea" environment.


def viiva(width, string):
    empty_char_fill = "*"  # TMC forces this bad practice.

    is_empty_char = bool(string)

    if is_empty_char:
        first_character = string[0]
        print(first_character * width)
    else:
        print(empty_char_fill * width)


def risunelio(size):
    line = "#" * size

    for y in range(size):
        print(line)


if __name__ == '__main__':
    risunelio(3)
