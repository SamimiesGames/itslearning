year = int(input("Vuosi: "))

if (year + 4) % 100 == 0 and (year + 4) % 400 != 0 or (year + 3) % 100 == 0 and (year + 3) % 400 != 0 or (year + 2) % 100 == 0 and (year + 2) % 400 != 0 or (year + 1) % 100 == 0 and (year + 1) % 400 != 0:
    num = year % 4
    print(f"Vuotta {year} seuraava karkausvuosi on {year + 8 - num}")

elif year % 100 == 0 and year % 400 == 0:
    print(f"Vuotta {year} seuraava karkausvuosi on {year + 4}")

elif year % 4 == 0 and year % 100 != 0:
    print(f"Vuotta {year} seuraava karkausvuosi on {year + 4}")

else:
    num = year % 4
    print(f"Vuotta {year} seuraava karkausvuosi on {year + 4 - num}")


# aloitusvuosi = int(input("Vuosi: "))
# vuosi = aloitusvuosi + 1
# while True:
#    if vuosi % 100 == 0:
#        if vuosi % 400 == 0:
#            break
#    elif vuosi % 4 == 0:
#        break
#
#    vuosi += 1
#
#print(f"Vuotta {aloitusvuosi} seuraava karkausvuosi on {vuosi}")