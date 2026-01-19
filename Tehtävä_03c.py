sukupuoli = input("Anna sukupuoli (nainen/mies): ")
hb = int(input("Anna hemoglobiiniarvo (g/l): "))
if sukupuoli == "nainen":
    if hb < 117:
        print("Alhainen hemoglobiiniarvo")
    elif hb <= 175:
        print("Normaali hemoglobiiniarvo")
    else:
        print("Korkea hemoglobiiniarvo")
elif sukupuoli == "mies":
    if hb < 134:
        print("Alhainen hemoglobiiniarvo")
    elif hb <= 195:
        print("Normaali hemoglobiiniarvo")
    else:
        print("Korkea hemoglobiiniarvo")
else:
    print("Virheellinen sukupuoli")
