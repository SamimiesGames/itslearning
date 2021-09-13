PREF_IDE = "Visual Studio Code"
WORST_IDE = "Word"

ERR_IDE_MSG = "ei ole hyvä"

ENVIRONMENTS = {
    PREF_IDE.lower(): ("loistava valinta!", True),
    WORST_IDE.lower(): ("surkea", False)
}


while True:
    environment = input("ENVIRONMENT: ").lower()

    if environment in ENVIRONMENTS:
        message, breaks = ENVIRONMENTS[environment]

        print(message)

        if breaks:
            break
    else:
        print(ERR_IDE_MSG)
