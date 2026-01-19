vuosi = int(input("Anna vuosi: "))
if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print("Karkausvuosi")
else:
    print("Ei karkausvuosi")
