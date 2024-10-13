def toon_inkomsten(inkomsten_dict, totaal):

    for item, bedrag in inkomsten_dict.items():
    print(f"{item}: {bedrag} euro")
    print("==========================")
    print(f"Totaal: {totaal} euro")
