import colorama 
import random 
from colorama import Fore,Back,Style
colorama.init()
from time import sleep
import os
if os.name == 'nt':
    _ = os.system('cls')
elif os.name == 'mac':
    _ = os.system('clear')
elif os.name =='posix':
    _ = os.system('clear')
else:
    _ = os.name('clear')
print(Fore.GREEN)
print("----------Tuttur Tuturabilirsen---------")
rastgele_sayı = random.randint(1,3)
a = 1
while a ==1:
    tahmin = input("Tahmininizi Alıyım Dostum :)\n-Tahmin;")
    tahmin = int(tahmin)
    if rastgele_sayı == tahmin:
         print("Şanlısın Kardeşşşş Nasıl Zihnimi Okudun Ama :))")
         rastgele_sayı1 = random.randint(1,5)
         print(Fore.CYAN + "Bunu Bulamazsın Çünkü Bu 2.Seviye")
         b=1
         while b ==1:
             tahmin1 =input("Tahmininizi Alıyım Dostum :)\n-Tahmin;")
             tahmin1 = int(tahmin1)
             if rastgele_sayı1 == tahmin1:
                 print("Ama Bu Kadar Da Zeki Olamazsın :((")
                 print(Fore.YELLOW + "3.Seviyeye Geçelim O Zaman")
                 rastgele_sayı2 = random.randint(1,10)
                 c = 1
                 while c ==1:
                     tahmin2 = input("Tahmininizi Alıyım Dostum :)\n-Tahmin;")
                     tahmin2 = int(tahmin2)
                     if rastgele_sayı2 == tahmin2:
                         print("Kanka Sen Beni Hackledin Mi Nasıl Biliyorsun?? :d")
                         print(Fore.RED + "EEEEE Seni 4.Seviyeye Geçiriyimde Gör (X_X)")
                         rastgele_sayı3 = random.randint(1,25)
                         d=1
                         while d==1:
                             tahmin3 = input("Tahmininizi Alıyım Dostum :)\n-Tahmin;")
                             tahmin3 = int(tahmin3)
                             if rastgele_sayı3 == tahmin3:
                                 print("İmdat Bu Adam Siber Dünyanın İçine Girmiş...Nasıl Biliyorsun Lannnnnnnnnnn(!_!)")
                                 print("Tebrik Ederim İnsan Oyunu Kazandın!!!!!")
                                 print("Uygulamadan Çıkılıyor....")
                                 sleep(3)
                                 exit()
                                 
                             else:
                                 print("Ağla İnsan En Son Seviyede Başa Döndün HAHAHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAHA")
                     else:
                         print("İnsan Değilmisin Hepiniz Benim Kadar Zeki Değilsiniz (O_O)")
                         print("Hey Ezik Sayı 1 İle 10 Arası (._.)")
             else:
                 print("Ezik Beni Yenemezsin Çünkü Ben 'Terbiyesiz Yazılımcı' HAHAHHAHAHAH ")
                 print("Tuttuğum Sayı 1 İle 5 Arası İnsan..")
    else:
         print("Kankacım Çok Yanlış Düşünüyorsun :/ ")
         print("Tuttuğum Sayı 1 İle 3 Arası :)")