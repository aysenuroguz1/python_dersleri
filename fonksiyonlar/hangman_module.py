import random

def kelime_sec(dosya_adi):
    with open(dosya_adi, "r", encoding="utf-8") as f:
        kelimeler = f.read().splitlines()
    return random.choice(kelimeler)


def tahmin_et(kelime):
    tahminler = []
    can = 5

    while can > 0:
        gizli = ""

        for harf in kelime:
            if harf in tahminler:
                gizli += harf + " "
            else:
                gizli += "_ "

        print(gizli)

        if "_" not in gizli:
            print("Kazandın 🎉")
            return

        harf = input("Harf gir: ")

        if harf in kelime:
            tahminler.append(harf)
        else:
            can -= 1
            print("Yanlış! Kalan can:", can)

    print("Kaybettin ❌ Kelime:", kelime)
