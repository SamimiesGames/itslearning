from statistics import mean


GRADES = [
    (28, 30, 5),
    (24, 27, 4),
    (21, 23, 3),
    (18, 20, 2),
    (15, 17, 1),
    (0, 14, 0)
]


def get_grade(summed):
    for low, high, grade in GRADES:
        if low <= summed <= high:
            return grade


def parse_points(points):
    grades = []

    for test_points, practice_points in points:
        if not test_points < 10:
            grades.append(get_grade(test_points + practice_points))

        else:
            grades.append(0)

    return grades


def get_points():
    data_pool = []

    while True:
        points = input("Koepisteet ja harjoitusten määrä:")

        if not points:
            break

        test_points, practice_points = points.split()

        test_points, practice_points = int(test_points), int(practice_points) // 10
        data_pool.append((test_points, practice_points))

    return data_pool


def main():
    points = get_points()
    grades = parse_points(points)
    sum_points = [x + y for x, y in points]
    average = mean(sum_points)
    acceptance_rate = len([x for x in grades if x != 0]) / len(grades)
    acceptance_rate *= 100
    print("Tilasto:")
    print(f"Pisteiden keskiarvo: {average:.1f}")
    print(f"Hyväksymisprosentti: {acceptance_rate:.1f}")

    print("Arvosanajakauma:")

    for index, value in enumerate(GRADES):
        index = len(GRADES) - 1 - index
        grade = value[-1]
        print(f"  {index}: {'*' * grades.count(grade)}")


main()
