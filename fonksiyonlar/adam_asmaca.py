import random

kelimeler = {
    "hayvanlar": ["kedi", "kuş", "tavşan", "fare"],
    "eşyalar": ["kalem", "silgi", "defter"],
    "taşıtlar": ["uçak", "vapur", "kamyon"]
}

# kategori seç
print("Kategoriler:")
print("1 - hayvanlar")
print("2 - eşyalar")
print("3 - taşıtlar")

secim = input("Kategori seçiniz (1-2-3): ")

if secim == "1":
    kategori = "hayvanlar"
elif secim == "2":
    kategori = "eşyalar"
elif secim == "3":
    kategori = "taşıtlar"
else:
    print("Geçersiz seçim")
    exit()

# rastgele kelime seç
kelime = random.choice(kelimeler[kategori])

tahmin_edilen = []
can = 5

print("\nOyun başlıyor!")

while can > 0:
    gizli_kelime = ""

    for harf in kelime:
        if harf in tahmin_edilen:
            gizli_kelime += harf + " "
        else:
            gizli_kelime += "_ "

    print("\nKelime:", gizli_kelime)

    if "_" not in gizli_kelime:
        print("🎉 Tebrikler kazandın!")
        break

    harf = input("Bir harf gir: ")

    if harf in kelime:
        print("Doğru tahmin!")
        tahmin_edilen.append(harf)
    else:
        can -= 1
        print("Yanlış tahmin! Kalan can:", can)

if can == 0:
    print("❌ Kaybettin! Kelime:", kelime)
