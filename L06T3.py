def muoka():
    lnimi = input("Anna luettavan tiedoston nimi: ")
    knimi = input("Anna kirjoitettavan tiedoston nimi: ")

    ltiedosto = open(lnimi, "r")
    ktiedosto = open(knimi, "w")
    lrivit = 0
    krivit = 0

    while True:
        rivi = ltiedosto.readline()[:-1]
        if rivi == "":
            break
        lrivit += 1
        if rivi.isalpha():
            ktiedosto.write(rivi.lower() + "\n")
            krivit += 1
    ltiedosto.close()
    ktiedosto.close()

    print("Luettiin", lrivit, "riviä tiedostosta '" + lnimi + "'.")
    print("Kirjoitettiin", krivit, "riviä tiedostoon '" + knimi + "'.")

def paaohjelma():
    muoka()
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
