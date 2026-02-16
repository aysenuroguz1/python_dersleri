class banka:
    def __init__(self):
        self.hesaplar={"iş":1000 ,"ev":500}


    def hesap_ekle(self,hesap_adi,miktar):
        self.hesaplar[hesap_adi]= miktar

    def bakiye(self):
        for i,j in self.hesaplar.items():
            print(f"{i} hesap bakiyesi:{j}")

    def para_yatir(self,hesap_adi,miktar):
        self.hesaplar[hesap_adi] += miktar
    
    def paara_cek(self,hesap_adi,miktar):
        if miktar > self.hesaplar[hesap_adi]:
            print("bakiye yetersiz")

        else:
            self.hesaplar[hesap_adi]-=miktar
    
            
