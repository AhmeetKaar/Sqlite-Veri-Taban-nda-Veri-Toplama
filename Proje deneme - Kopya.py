import time


from kütüphanem import *

print("""

Kütüphane Programına Hoşgeldiniz.

İşlemler ;

1.Kitapları Göster

2.Kitap Sorgulama

3.Kitap Ekle

4.Kitap Sil

5.Baskı Yükselt

Çıkmak İçin 'q' ya basın.

""")


kütüphanem = Kütüphane()


while True:

    işlem = input("Yapacağınız İşlemi Giriniz: ")


    if işlem == "q":
        print("Programdan Çıkış Yapılıyor..")
        print("Yine bekleriz..")
        break


    elif işlem == "1":

        print("Kitap Bilgileri Açılıyor..")
        time.sleep(1)

        kütüphanem.kitaplarıGöster()

    elif işlem == "2":

        isim = input("Hangi Kitabı İstiyorsunuz: ")
        print("Kitap Sorgulanıyor..")
        time.sleep(2)


    elif işlem == "3":

        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yayınevi: ")
        tür = input("Tür: ")
        baskı = int(input("Baskı: "))


        yeniKitap = Kitap(isim,yazar,yayınevi,tür,baskı)

        print("Kitap Ekleniyor..")
        time.sleep(2)

        kütüphanem.kitapEkle(yeniKitap)
        print("Kitap Eklendi..")



    elif işlem == "4":

        isim = input("Hangi Kitabı Silmek İstiyorsunuz: ")

        cevap = input("Silmek İstediğinize Emin Misiniz : (E/H) ")

        if cevap == "E":
            print("Kitap Siliniyor..")
            time.sleep(2)

            kütüphanem.kitapSil(isim)
            print("Kitap Silindi..")


    elif işlem == "5":
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz: ")

        print("Baskı Yükseltiliyor..")
        time.sleep(2)
        kütüphanem.baskıYükselt(isim)
        print("Baskı Yükseltildi..")



    else:
        print("Geçersiz işlem..")
        print("Lütfen tekrar programa giriş yapınız..")











