def valikko(lista):
    print("Ostoslistasi sisältää seuraavat tuotteet:")
    print(lista)
    print("Voit valita alla olevista toiminnoista:")
    print("1) Lisää")
    print("2) Poista")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

def paaohjelma():
    ostoslista = []
    while True:
        toiminta = valikko(ostoslista)
        if toiminta == 1:
            tuote = input("Anna lisättävä tuote: ")
            ostoslista.append(tuote)
        elif toiminta == 2:
            print("Ostoslistassasi on", len(ostoslista), "tuotetta.")
            pois = int(input("Anna poistettavan tuotteen järjestysnumero: "))
            ostoslista.remove(ostoslista[pois-1])
        elif toiminta == 0:
            print("Sinulta jäi ostamatta seuraavat tuotteet:")
            print(ostoslista)
            print("Kiitos ohjelman käytöstä.")
            break
        else:
            print("Tunnistamaton valinta.")
        print()
    return None

paaohjelma()
