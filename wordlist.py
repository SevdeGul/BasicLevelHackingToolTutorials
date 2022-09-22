#!/usr/bin/env python

import os 
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDLIST")
print("""
Word List Aracına Hoş  Geldiniz... :)

""")

mini = input("Minimum Karakter Sayısını Girin: ")
maxi = input("Maksimum Karakter Sayısını Girin: ")
karakter = input("İstediğiniz Karakterleri Girin: ")
kayityeri = input("Kaydediecek Yeri Girin: ")

os.system("crunch " + mini + " " + maxi + " " + karakter + " -o " + kayityeri )

print("İşlem Başarılı") 
