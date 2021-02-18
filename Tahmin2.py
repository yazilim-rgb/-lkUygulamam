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
türkiyenin_illeri =["Adana","Adıyaman","Afyon","Ağrı","Amasya","Ankara","Antalya","Artvin","Aydın","Balıkesir","Bilecik","Bingöl","Bitlis","Bolu","Burdur","Bursa","Çanakkale","Çankırı","Çorum","Denizli"]
türkiyenin_illeri1=["Diyarbakır","Edirne","Elazığ","Erzincan","Erzurum","Eskişehir","Gaziantep","Giresun","Gümüşhane","Hakkari","Hatay","Isparta","Mersin","İstanbul","İzmir","Kars","Kastamonu","Kayseri","Kırklareli","Kırşehir"]
türkiyenin_illeri2=["Kocaeli","Konya","Kütahya","Malatya","Manisa","Kahramanmaraş","Mardin","Muğla","Muş","Nevşehir","Niğde","Ordu","Rize","Sakarya","Samsun","Siirt","Sinop","Sivas","Tekirdağ","Tokat","Trabzon"]
türkiyenin_illeri3=["Tunceli","Şanlıurfa","Uşak","Van","Zonguldak","Aksaray","Bayburt","Karaman","Kırıkkale","Batman","Şırnak","Bartın","Ardahan","Iğdır","Yalova","Karabük","Kilis","Osmaniye","Düzce"]
print(Fore.RED+"---------Bil Bakalım Türkiyenin İlleri--------")
print(Fore.MAGENTA)
print("""
|****************************|
|     Ad:Terbiyesiz          |
|  Soyad:Robot               |
|   Amaç:Oyun Oynamak        |
|     NOT:81 İl Var          |
|     NOT:İlk Harf Büyük Yaz |
|                            |
|                            |
|                            |
|                            |
|****************************|
""")
rastgele = random.choice(türkiyenin_illeri)
rastgele1 = random.choice(türkiyenin_illeri1)
rastgele2 = random.choice(türkiyenin_illeri2)
rastgele3 = random.choice(türkiyenin_illeri3)
a = 1
deneme = 0
while a ==1:
    tahmin=input(Fore.CYAN + "Bil Bakalım Hangi Şehirdeyim ??\n-Bulunduğum Şehir;")
    deneme += 1
    if (tahmin == rastgele) or (tahmin == rastgele1) or (tahmin == rastgele2) or (tahmin == rastgele3):
        print(Fore.CYAN + str(deneme) + " Kez Denemişsin Karşim Ama Sonunda Kazandın :))")
        print(Fore.GREEN + "Uygulamadan Çıkılıyor....")
        print("-5..")
        sleep(1)
        print("-4..")
        sleep(1)
        print("-3..")
        sleep(1)
        print("-2..")
        sleep(1)
        print("-1..")
        sleep(1)
        print("-0..")
        print("-Terbiyesiz Yazılımcı İyi Günler Diler...")
        sleep(2)
        if os.name == 'nt':
              _ = os.system('cls')
        elif os.name == 'mac':
              _ = os.system('clear')
        elif os.name =='posix':
              _ = os.system('clear')
        else:
              _ = os.name('clear')
        exit()
        if os.name == 'nt':
              _ = os.system('python Tahmin2.py')
        elif os.name == 'mac':
              _ = os.system('python Tahmin2.py')
        elif os.name =='posix':
              _ = os.system('python Tahmin2.py')
        else:
              _ = os.name('python Tahmin2.py')
    else:
        if deneme ==1:
             print(Fore.YELLOW + "Üzülme Kanka Hiç Kolay Değil..") 
             print("İpucu;" +((rastgele[:1]) and (rastgele1[:1]) and (rastgele2[:1]) and (rastgele3[:1])))
        if deneme == 2:
            print(Fore.YELLOW + "Üzülme Kanka Hiç Kolay Değil..") 
            print("İpucu;" +((rastgele[:2]) and (rastgele1[:2]) and (rastgele2[:2]) and (rastgele3[:2])))
        elif deneme == 5:
            print(Fore.YELLOW + "Üzülme Kanka Hiç Kolay Değil..") 
            print("İpucu;" +((rastgele[:3]) and (rastgele1[:3]) and (rastgele2[:3]) and (rastgele3[:3])))
        elif  deneme ==10:
            print(Fore.YELLOW + "Üzülme Kanka Hiç Kolay Değil..") 
            print("İpucu;" +((rastgele[:4]) and (rastgele1[:4]) and (rastgele2[:4]) and (rastgele3[:4])))
        elif  deneme ==17:
            print(Fore.YELLOW + "Üzülme Kanka Hiç Kolay Değil..") 
            print("İpucu;" +((rastgele[:5]) and (rastgele1[:5]) and (rastgele2[:5]) and (rastgele3[:5])))
        
