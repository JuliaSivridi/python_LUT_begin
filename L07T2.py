class AUTO:
    merkki = ""
    lkm = 0

def kysy_auto():
    auto = AUTO()
    auto.merkki = input("Anna automerkki: ")
    auto.lkm = input("Anna automerkin lukumäärä varastossa: ")
    return auto

def tulosta_auto(auto):
    print("Varastossa on nyt "+auto.merkki+"-merkkisiä autoja "+auto.lkm+" kpl.")

def paaohjelma():
    vauto = kysy_auto()
    tulosta_auto(vauto)
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
