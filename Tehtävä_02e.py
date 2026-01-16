leiviskat=float(input("Anna leiviskät:"))
naulat=float(input("Anna naulat:"))
luodit=float(input("Anna luodit:"))
kokonaisluodit=leiviskat*20*32 + naulat*32 + luodit
kokokg=int(kokonaisluodit * 13.3//1000)
grammat=kokonaisluodit * 13.3 % 1000
print(f"Massa nykymittojen mukaan:\n{kokokg} kilogrammaa ja {grammat:.2f} grammaa.")