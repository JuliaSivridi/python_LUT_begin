jono = input("Anna pitkä merkkijono: ")
print("Merkkijono oli", len(jono), "merkkiä pitkä.")
print("")

print("Antamasi merkkijonon viisi ensimmäistä kirjainta ovat", jono[:5:])
print("Viisi viimeistä kirjainta ovat", jono[-5::])
print("Kirjaimet 2, 3, 4 ja 5 ovat", jono[1:5])
print("Joka toinen kirjain alkaen toisesta kirjaimesta:", jono[1::2])
print("")

print("Annettu merkkijono '", jono, "' on takaperin '", jono[::-1], "'.", sep="")
print("")

aloituspaikka = int(input("Anna aloituspaikka: "))
lopetuspaikka = int(input("Anna lopetuspaikka: "))
siirtymä = int(input("Anna siirtymä: "))
print("Antamillasi asetuksilla", jono, "tulostuu näin:", jono[aloituspaikka:lopetuspaikka:siirtymä])
