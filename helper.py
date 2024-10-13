def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} * ")
    print(lengte * "*")
    print()

def fooi_pp(bedrag,personen):
        bedrag_pp = bedrag/personen
        return f"Het bedrag per persoon is{bedrag_pp} euro"
    
b = int(input("Welk bedrag zit er in de fooienpot?" ))
p = int(input("Over hoeveel mensen moet de pot verdeeld worden?" ))

print(fooi_pp(b,p))

def ondersteep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

from boekhouding import inkomsten

def bereken_totaal(inkomsten_dict):
 totaal = 0

 for item, bedrag in inkomsten_dict.items():
     totaal += bedrag
    return totaaal