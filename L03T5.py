pituus = int(input("Anna pituus (senteissä): "))
massa = int(input("Anna paino (kilogrammoissa): "))

osa = ((pituus / 100) ** 2)
painoindeksi = round(massa / osa, 1)

if painoindeksi < 15:
    print("Painoindeksi on", painoindeksi, "(Sairaalloinen alipaino)")
elif 15 <= painoindeksi < 17:
    print("Painoindeksi on", painoindeksi, "(Merkittävä alipaino)")
elif 17 <= painoindeksi < 18.5:
    print("Painoindeksi on", painoindeksi, "(Normaalia alhaisempi paino)")
elif 18.5 <= painoindeksi < 25:
    print("Painoindeksi on", painoindeksi, "(Normaali paino)")
elif 25 <= painoindeksi < 30:
    print("Painoindeksi on", painoindeksi, "(Lievä ylipaino)")
elif 30 <= painoindeksi < 35:
    print("Painoindeksi on", painoindeksi, "(Merkittävä ylipaino)")
elif 35 <= painoindeksi < 40:
    print("Painoindeksi on", painoindeksi, "(Vaikea ylipaino)")
elif 40 <= painoindeksi:
    print("Painoindeksi on", painoindeksi, "(Sairaalloinen ylipaino)")

tavoiteindeksi = float(input("Anna tavoiteindeksi: "))
uus_massa = tavoiteindeksi * osa
if tavoiteindeksi < painoindeksi:
    print("Painoa tulisi tiputtaa", round(massa - uus_massa, 1), "kilogrammaa.")
elif tavoiteindeksi > painoindeksi:
    print("Painoa tulisi kerätä", round(uus_massa - massa, 1),"kilogrammaa.")

print("Kiitos ohjelman käytöstä.")
