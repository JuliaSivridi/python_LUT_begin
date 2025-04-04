def kysynimi(tnimi):
    while True:
        nimi = input("Anna tiedostoon tallennettava nimi (0 lopettaa): ")
        if nimi == "0":
            break
        tiedosto = open(tnimi, "a")
        tiedosto.write(nimi+"\n")
        tiedosto.close()

def tulostanimi(tnimi):
    print("Tiedostoon '"+tnimi+"' on tallennettu seuraavat nimet:")
    tiedosto = open(tnimi, "r")
    while True:
        rivi = tiedosto.readline()
        if rivi == "":
            break
        print(rivi, end="")
    tiedosto.close()

def paaohjelma():
    tiedoston_nimi = input("Anna tallennettavan tiedoston nimi: ")
    kysynimi(tiedoston_nimi)
    tulostanimi(tiedoston_nimi)
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
