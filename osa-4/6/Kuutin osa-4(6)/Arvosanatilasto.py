import math


def feed():
    grade_points = []

    exercise_points = []

    input1 = input("Koepisteet ja harjoitusten määrä: ")

    while input1:
        input_list = input1.split(" ")

        grade_points.append(int(input_list[0]))

        exercise_points.append(int(input_list[1]))

        input1 = input("Koepisteet ja harjoitusten määrä: ")

    return grade_points, exercise_points


def sum_points(grade_points, exercise_points):
    total_points = []

    i = 0

    while i < len(exercise_points):
        total_points.append(math.floor(

            exercise_points[i] / 10) + grade_points[i])

        i += 1

    return total_points


def distribution(total_points, grade_points):
    array = [0] * 6

    i = 0

    while i < len(total_points):

        if total_points[i] <= 14 or grade_points[i] < 10:

            array[0] += 1



        elif 15 <= total_points[i] <= 17:

            array[1] += 1



        elif 18 <= total_points[i] <= 20:

            array[2] += 1



        elif 21 <= total_points[i] <= 23:

            array[3] += 1



        elif 24 <= total_points[i] <= 27:

            array[4] += 1



        elif 28 <= total_points[i] <= 30:

            array[5] += 1

        i += 1

    return array


def final_print(total_points, grade_points):
    print("Tilasto:")

    sum = 0

    for x in total_points:
        sum += x

    print("Pisteiden keskiarvo: {:.1f}".format(sum / len(total_points)))

    i = 0

    fail = 0

    while i < len(total_points):

        if total_points[i] <= 14 or grade_points[i] < 10:
            fail += 1

        i += 1

    print("Hyväksymisprosentti: {:.1f}".format(

        (len(total_points) - fail) / len(total_points) * 100))

    array = distribution(total_points, grade_points)

    print("Arvosanajakauma:")

    print(f"  5: {'*' * array[5]}")

    print(f"  4: {'*' * array[4]}")

    print(f"  3: {'*' * array[3]}")

    print(f"  2: {'*' * array[2]}")

    print(f"  1: {'*' * array[1]}")

    print(f"  0: {'*' * array[0]}")


def main():
    grade_points, exercise_points = feed()

    total_points = sum_points(grade_points, exercise_points)

    final_print(total_points, grade_points)


main()