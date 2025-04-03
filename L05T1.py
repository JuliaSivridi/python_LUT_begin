def ens():
    print("Nyt olemme tulosta-aliohjelmassa")
    print("Tämä aliohjelma tulostaa vain tekstiä.")
    print("Sopii hyvin valikon tulostamiseen.")
    return None

def toinen(luku):
    print("Aliohjelmassa:", luku)
    print("Aliohjelmassa luvun neliö:", luku ** 2)

def kolmas(e, s):
    return e + " " + s

print("Ensimmäinen vaihe:")
ens()

print("\nToinen vaihe:")
luku = int(input("Anna luku: "))
print("Päätasolla ennen aliohjelmaa:", luku)
toinen(luku)
print("Päätasolla aliohjelman jälkeen:", luku)

print("\nKolmas vaihe:")
etunimi = input("Anna etunimi: ")
sukunimi = input("Anna sukunimi: ")
nimi = kolmas(etunimi, sukunimi)
print("Etunimi '", etunimi, "' ja sukunimi '", sukunimi, "' muodostavat nimen '", nimi, "'.", sep="")

print("Kiitos ohjelman käytöstä.")
