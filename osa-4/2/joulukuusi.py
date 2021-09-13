def joulukuusi(height):
    print("joulukuusi!")

    width = height

    for i in range(height):
        value = i + 1
        offset = width - value

        padding_right = " " * offset
        shape = "*" * value

        if value > 1:
            shape += shape[:-1][::-1]  # clone the other side of the tree

        print(padding_right + shape)

    padding = " " * (width - 1)
    print(f"{padding}*")


if __name__ == '__main__':
    joulukuusi(5)
