SIGTERM = "exit"
OPTIONS = {
    "l": lambda arr: arr.append(len(arr) + 1),
    "p": lambda arr: arr.pop(-1),
    "x": lambda arr: SIGTERM,
}

array = []
print("Lista on nyt", array)

while True:
    option = input("(l)isää, (p)oista, e(x)it: ")

    function = OPTIONS[option]
    ret = function(array)

    if ret == SIGTERM:
        break

    print("Lista on nyt", array)


print("Moi!")
