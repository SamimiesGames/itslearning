PREF_IDE = "Visual Studio Code"


while True:
    environment = input("ENVIRONMENT: ")

    if environment != PREF_IDE:
        print("loistava valinta!")
        break
    else:
        print("ei ole hyvä")
