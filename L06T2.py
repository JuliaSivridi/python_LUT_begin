lnimi = input("Anna luettavan tiedoston nimi: ")
knimi = "L06T2_palindromit.txt"

ltiedosto = open(lnimi, "r")
ktiedosto = open(knimi, "w")
while True:
    rivi = ltiedosto.readline()[:-1]
    if rivi == "":
        break
    if rivi.isdigit():
        print("Rivi '"+rivi+"' on numerorivi.")
    else:
        if rivi == rivi[::-1]:
            print("Rivi '"+rivi+"' on palindromi.")
            ktiedosto.write(rivi + "\n")
        else:
            print("Rivi '"+rivi+"' ei ole palindromi.")
ltiedosto.close()
ktiedosto.close()

print("Kiitos ohjelman käytöstä.")
