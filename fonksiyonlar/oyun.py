import random

def kelime_sec(dosya):
    with open(dosya, "r", encoding="utf-8") as f:
        kelimeler = f.read().splitlines()
    return random.choice(kelimeler)

def tahmin_et(kelime):
    print("Tahmin başlasın")
