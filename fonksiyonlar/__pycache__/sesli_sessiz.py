# verilen bir kelimede sesli sessiz harfleri bulan fonksiyon..
import random 
def sesli_sessiz(kelime):
    sesliler="aeıiuüoö"
    sesli=0
    sessiz=0

    for i in kelime:
        if i in sesliler:
            sesli+=1
          
        else:
            sessiz+=1
            
    return sesli,sessiz

#----------------------------------------------

if __name__== "__main__":

    kelime=input("kelime giriniz")
    sesli,sessiz = kelime= sesli_sessiz(kelime)
    print(f"sesli harf sayısı :{sesli} ,sessiz harf sayısı :{sessiz}")

    print(__name__)