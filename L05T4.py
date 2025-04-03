def tulosta(s):
    for i in range(len(s)):
        print(s[i:])

def valitse():
    sana = ""
    while True:
        print("\nKäytettävissä olevat toiminnot:", "1) Määritä sana", "2) Tulosta sana alusta loppuun", "3) Tulosta sana lopusta alkuun", "0) Lopeta", sep="\n")
        valinta = input("Valintasi: ")
        if valinta == "1":
            sana = input("Anna sana: ")
        elif valinta == "2":
            tulosta(sana)
        elif valinta == "3":
            tulosta(sana[::-1])
        elif valinta == "0":
            break
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.")

def paaohjelma():
    print("Tämä ohjelma tulostaa sanan käyttäjän haluamalla tavalla.", end="")
    valitse()
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
