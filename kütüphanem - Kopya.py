import sqlite3

import time


class Kitap():


    def __init__(self,isim,yazar,yayınevi,tür,baskı):

        self.isim = isim
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tür = tür
        self.baskı = baskı

    def __str__(self):

        return "Kitap İsmi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\n".format(self.isim,self.yazar,self.yayınevi,self.tür,self.baskı)



class Kütüphane():


    def __init__(self):

        self.baglantıOlustur()


    def baglantıOlustur(self):

        self.baglanti = sqlite3.connect("kütüphanem.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists kitaplar (isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()


    def baglantıyıKes(self):

        self.baglanti.close()

    def kitaplarıGöster(self):

        sorgu = "Select * From kitaplar"

        self.cursor.execute(sorgu)

        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0) :

            print("Kütüphanede kitap bulunmamaktadır...")

        else:
            for i in kitaplar:

                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])

                print(kitap)


    def kitapSorgula(self,isim):


        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0) :

            print("Böyle bir kitap bulunmamaktadır..")

        else:
            kitap = Kitap (kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])

            print(kitap)



    def kitapEkle(self,kitap):

        sorgu = "Insert into kitaplar Values (?,?,?,?,?)"

        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.tür,kitap.baskı))

        self.baglanti.commit()



    def kitapSil(self,isim):

        sorgu = "Delete From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        self.baglanti.commit()

    def baskıYükselt(self):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu, (isim ,))

        kitaplar = self.cursor.fetchall()  #Dönen tüm satırları liste şeklinde almamızı sağlar

        if len(kitaplar) == 0:
            print("Böyle bir kitap bulunmuyor..")


        else:

            baskı = kitaplar[0][4]

            baskı += 1

            sorgu2 = "Update kitaplar set baskı = ? where isim = ?"

            self.cursor.execute(sorgu2,(baskı,isim))

            self.baglanti.commit()