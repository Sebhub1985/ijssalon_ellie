def mijn_functie_1(a):
    return a * a
  
 def mijn_functie_2(a,b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a/b)
    return uitvoer_lijst

print(mijn_functie_1(3))
print(mijn_functie_2(3,2))