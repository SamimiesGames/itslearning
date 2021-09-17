def pisin_naapurijono(array):
    sub_arrays = []
    sub_array = []
    i_len = len(array) - 1

    for index, value in enumerate(array):
        neighbour = index + 1
        neighbour_exists = neighbour <= i_len

        if not neighbour_exists:
            break

        neighbour_item = array[neighbour]
        is_neighbour = abs(value - neighbour_item) == 1
        has_third_neighbour = neighbour + 1 <= i_len
        new_neighbour = len(sub_array) == 0

        if is_neighbour:
            if new_neighbour:
                sub_array.append(value)

            sub_array.append(neighbour_item)

            if has_third_neighbour:
                continue

        if sub_array:
            sub_arrays.append(sub_array)
            sub_array = []

    return len(max(sub_arrays, key=len))


if __name__ == '__main__':
    print(pisin_naapurijono([1, 2, 3, 5, 6, 9, 10]))
