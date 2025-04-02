print("Tämä ohjelma etsii antamistasi kokonaisluvuista pienimmän.")
min = 100
while True:
    luku = int(input("Anna kokonaisluku väliltä 1-100 (-1 lopettaa): "))
    if luku == -1:
        break
    elif luku not in range(1,101):
        print("Luku ei ollut pyydetyllä välillä, yritä uudestaan, -1 lopettaa.")
    else:
        if luku < min:
            min = luku

print("Antamistasi luvuista pienin oli", min)

print("Kiitos ohjelman käytöstä.")
