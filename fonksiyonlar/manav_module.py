class manav:
    def __init__(self):
        self.liste = {}      # alınan ürünler
        self.toplam = 0      # toplam tutar

    # Ürün ekleme
    def urun_al(self, urun_adi, kg):
        self.liste[urun_adi] = kg

    # Fiş yazdırma
    def fis_yazdir(self):

        urun_fiyat = {}

        # Ürün fiyatlarını dosyadan okuma
        try:
            with open("urunler.txt", "r") as dosya:
                for satir in dosya:
                    satir = satir.strip()
                    parca = satir.split(",")

                    urun = parca[0]
                    fiyat = int(parca[1])

                    urun_fiyat[urun] = fiyat

        except:
            print("urunler.txt dosyası bulunamadı.")
            return

        # Fiş oluşturma
        with open("fis.txt", "w") as fis:

            for urun, kg in self.liste.items():

                if urun in urun_fiyat:

                    tutar = urun_fiyat[urun] * kg
                    self.toplam += tutar

                    fis.write(f"{urun} {kg} kg = {tutar} TL\n")

            fis.write("----------------------\n")
            fis.write(f"Toplam Tutar ==> {self.toplam} TL\n")

        print("Fiş başarıyla oluşturuldu.")
