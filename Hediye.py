from time import sleep
import colorama
from colorama import  Fore,Back,Style
colorama.init()
print(Fore.CYAN)
isim = input("İsmini Girsene Sana Bir Süprizim Olucak :))\n-İsminiz Lütfen;")
print(Fore.YELLOW)
print(isim+" Süpriz Yükleniyor....")
while True:
       print(Fore.BLUE)
       print(isim.upper()+" Seni Kandırdım Ağla Moruk Hahahahahaha")
       sleep(0.5)
