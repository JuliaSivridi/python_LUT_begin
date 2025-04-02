nimi = ""

while True:
    print("Tämä ohjelma pystyy toteuttamaan seuraavat toiminnot:", "1) Anna nimi", "2) Tulosta nimi", "0) Lopeta", sep="\n")
    valinta = input("Anna valintasi: ")
    if valinta == "1":
        nimi = input("Anna nimi: ")
    elif valinta == "2":
        if nimi == "":
            print("Nimeä ei ole vielä annettu.")
        else:
            print("Nimi on '", nimi, "'.", sep="")
    elif valinta == "0":
        break
    else:
        print("Tuntematon valinta, yritä uudestaan.")

print("Kiitos ohjelman käytöstä.")
