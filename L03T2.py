ok = input("Haluatko kirjautua sisään (k/K): ")
if ok == "k" or ok == "K":
    nimi = input("Anna nimi: ")
    salasana = input("Anna salasana: ")
    if nimi == "Matti" and salasana == "salasana":
        print("Käyttäjä tunnistettu.")
    else:
        print("Antamasi nimi oli", len(nimi), "merkkiä pitkä, mutta se tai salasana ei ollut oikein.")

print("Kiitos ohjelman käytöstä.")
