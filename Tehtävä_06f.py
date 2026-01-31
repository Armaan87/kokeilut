import math

def yksikkohinta(halkaisija_cm, hinta):
    sade_m = (halkaisija_cm / 100) / 2
    pinta_ala = math.pi * sade_m * sade_m
    return hinta / pinta_ala

h1 = float(input("Pizza 1 halkaisija (cm): "))
p1 = float(input("Pizza 1 hinta (€): "))

h2 = float(input("Pizza 2 halkaisija (cm): "))
p2 = float(input("Pizza 2 hinta (€): "))

y1 = yksikkohinta(h1, p1)
y2 = yksikkohinta(h2, p2)

if y1 < y2:
    print("Pizza 1 on parempi vastine rahalle")
else:
    print("Pizza 2 on parempi vastine rahalle")
