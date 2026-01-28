luku = int(input("Anna kokonaisluku: "))
if luku < 2:
    print("Ei ole alkuluku")
else:
    i = 2
    while i < luku and luku % i != 0:
        i += 1
    if i == luku:
        print("On alkuluku")
    else:
        print("Ei ole alkuluku")
