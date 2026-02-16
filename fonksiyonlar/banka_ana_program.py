from banka_module import banka as b

menu ="""
1 bakiye sorma
2 para çekme
3 para yatırma
4 hesap ekle
5 çıkış
"""
isim =input("isminiz")
kisi=b()

while True:
  
  
    print(menu)
    secim=input("seçiminiz:")

    if secim=="5":
        break
    elif secim=="1":
        kisi.bakiye()

    elif secim =="2":
        hesap=input("hesap adını giriniz:")
        miktar=int(input("kaç lira çekeceksiniz"))
        kisi.para_cek(hesap,miktar)

    elif secim=="3":
        hesap=input("hesap adını giriniz:")
        miktar=int(input("kaç lira yatıracaksınız"))
        kisi.para_yatir(hesap,miktar)
        
    elif secim=="4":
        hesap=input("hesap adını giriniz:")
        miktar=int(input("kaç lira hesap açıcaksınız"))
        kisi.hesap_ekle