import camasir_makinesi as yy

menu = """
1- az kirli
2- çok kirli
"""

print(menu)

secim = input("Seçiminiz: ")

if secim == "1":
    print("yıkama yapılıyor")
    yy.yikama({"sure": 20, "isi": 40, "su_miktari": 5})

    print("sıkma yapılıyor")
    yy.sikma({"sure": 5})

    print("durulama yapılıyor")
    yy.yikama({"sure": 5, "isi": 20, "su_miktari": 10})

    print("sıkma yapılıyor")
    yy.sikma({"sure": 10})

    print("yıkama işlemi bitti..")

elif secim == "2":
    print("ön yıkama yapılıyor")
    yy.yikama({"sure": 5, "isi": 40, "su_miktari": 5})

    print("sıkma yapılıyor")
    yy.sikma({"sure": 5})

    print("yıkama yapılıyor")
    yy.yikama({"sure": 45, "isi": 50, "su_miktari": 5})

    print("durulama yapılıyor")
    yy.yikama({"sure": 5, "isi": 20, "su_miktari": 10})

    print("sıkma yapılıyor")
    yy.sikma({"sure": 10})

    print("yıkama işlemi bitti..")

else:
    print("Geçersiz seçim")
