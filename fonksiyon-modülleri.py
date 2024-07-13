import math

sonuc=math.fabs(4)
print(sonuc)

from math import factorial, sqrt
sonuc= factorial(5)
sonuc1= sqrt(4)
print(sonuc)
print(sonuc1)

from math import *
sonuc= factorial(5)
sonuc1= sqrt(4)
print(sonuc)
print(sonuc1)

def cember_cevre(r):
    return 2*3.14*r
def dairealan(r):
    return 3.14*r*r



#random,uniform fonksiyonları
# randint ve random fonksiyonları
#choice, shuffle ve sample fonksiyonları

import random
for i in range(10):
    print(random.random()) # rastgele ondalık sayı üretir
for i in range(10):
    print(random.uniform(10,30)) #bizim belirlediğimiz sayılar arasında ondalık sayı yazdırır.

for i in range(10):
    print(random.randint(1,5)) #girdiğmiz sayılar arasında rastgele tam sayılar yazdırır.

for i in range(10):
    print(random.randrange(1,18,1))# BİRDEN BAŞLAYIP ONA KADAR ÜÇER ÜÇER ATLAYARAK YAZDIRIR.
#listelerde kullanılanlar.

liste=["siyah","beyaz","turuncu","yeşil","gri"]
print(random.choice(liste)) #listeden rastgele renk seçiyor.

random.shuffle(liste) #listenin yerlerini değştiriyor.
print(liste)

print(random.sample(liste,3)) # verdiğin listeden istediğin kadar eleman seçiyor.


#örnek soru
zarlar={1:0,2:0,3:0,4:0,5:0,6:0} #sözlük oluşturuldu.
for i in range(100000):
    zar=random.randint(1,6)
    zarlar[zar] +=1
for zar  in zarlar:
    print(f"{zar} gelme olasılığı: {zarlar[zar]/100000}") 

alti_alti=0
deneme_sayisi=0
while True:
    deneme_sayisi+=1
    zar1=random.randint(1,6)
    zar2=random.randint(1,6)
    if zar1==6 and zar2==6:
        alti_alti+=1
    if alti_alti==10:
        print(f"10 kere 6-6 gelmesi için zarlar {deneme_sayisi} kadar atıldı.")
        break

import time
zaman=time.time()
print(zaman) #noktadan önceki iki sayı 1 ocak 1975 den beri geçen zamanın değeridir.

baslangic=time.time()
liste=[]
for i in range(1000000):
    liste.append(i)
bitis=time.time()
print(bitis-baslangic) #aradan ne kadar zaman geçtiğini yazdırıyor.

zaman= time.ctime(20000000)
print(zaman) #şuanki tarihi verir içi boş olursa. içini doldurursan başlangıç tarihinden o kadar saniye sonrasını gösterir.

zaman=time.localtime()
print(zaman) #zamanın değişik biçimlerini ayrı ayrı yazdırır.
 
zaman= time.asctime()
print(zaman) #içini doldurursan hata alırsın.

zaman=time.strftime("%d:%m:%Y %H:%M:%S")# hiçbir şey yazmazsan geçerli zamanı alır ama istediğin şekildede yazdırabilirsin.
print(zaman) # %d= gün %Y= yıl %H=saat %M:dakika %S=saniye %I=12lik saat dilimi.
#en kullanışlısı. formatlayabildiğimiz içerik

print("program başlatıldı.")
time.sleep(0) #program girdiğiniz deger kadar durdurulur. web sayfalarında kullanılabilir.
print("program sonlandı.")


from datetime import date
bugun=date.today()
print(bugun)
#sınıfın özellikleri gun,ay,yıl şeklinde çağırıyorsun
print(type(bugun))
print(bugun.day)
print(bugun.month)
print(bugun.year)
print(bugun.weekday())

gecmis_tarih=date(2015,8,13)
print(gecmis_tarih)
print(gecmis_tarih.weekday())

gecen_zaman=bugun-gecmis_tarih
print(gecen_zaman)
print(type(gecen_zaman))

#suan=datetime.now()  çalıştıramadım.
#ctime hangi saati tarihi göstereceğini bilmiyor. tarihleri sen yazarsan yazdırır.bir değişken üzerinden çağırman gerekir.
print(bugun.ctime())
#örnek soru
#1900 ve 2000 31 aralığa kadar kaç sefer ilk ayın pazartesiye denk geldiğini bul.

pazar_sayisi=0
for yil in range(1901,2001):
    for ay in range(1,13):
        if date(yil,ay,1).weekday()==6:
            pazar_sayisi+=1
print(pazar_sayisi)

#os modeli anlaşılmadı.
"""
import os
#os modülü yardımı ile dosya sisteminde gezinme , klasör içeriği görüntüleme
#dosya yeni adlandırma, klasörlere ayırabilirsin.
print(os.getcwd())# hangi klasörde oldugunu gösterir.
#os.chdir("") #klasör değiştirmeye yarar.
#print(os.getcwd())
print(os.listdir())
for dosya in os.listdir():
    print(dosya)

#os.mkdir("denemeKlasörü")#yeni klasör oluşturuldu.tekrar çalıştırırsan hata alırsın.
#iç içe klasör oluşturma: istediğin kadar oluşturabilirsin

#os.makedirs("deneme1/deneme2")

os.rmdir("denemeKlasörü") #dosya silmeye yarar.

os.removedirs("deneme1/deneme2")#içeriği boş olanları siler.
os.chdir("")
print(os.listdir())

"""




from datetime import date

pazar_günü=0
for yil in range(1901,2001):
    for ay in range(1,13):
        if date(yil,ay,1).weekday()==6:
         pazar_günü+=1
print(pazar_günü)


