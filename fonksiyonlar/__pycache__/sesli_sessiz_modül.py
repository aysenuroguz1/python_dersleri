import sesli_sessiz as sesli_sessiz_modül

kelime=input("bir kelime giriniz:")
sesli,sessiz = sesli_sessiz_modül.sesli_sessiz(kelime)
print(f"{kelime} kelimesinde toplam {sesli}, adet sesli harf ve {sessiz} adet sessiz harf vardır.")