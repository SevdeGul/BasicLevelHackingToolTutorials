#!/usr/bin/env python

import os 
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDPRESS TARAMA")
print("""
Wordpress Tarama Aracına Hoş  Geldiniz... :)

1) Hızlı Tarama
2) Eklenti Tarama
3) Tema Tarama
4) Yönetici Kullanıcı Adı Tarama

""")

islemno = input("İşlem Numarası Girin: ")

if(islemno == "1"):
	site = input("Site Adresi Girin: ")
	os.system("wpscan --url " + site )
elif(islemno == "2"):
	site = input("Site Adresi Girin: ")
	os.system("wpscan --url " + site + " --enumerate p" )
elif(islemno == "3"):
	site = input("Site Adresi Girin: ")
	os.system("wpscan --url " + site + " --enumerate t" )
elif(islemno == "4"):
	site = input("Site Adresi Girin: ")
	os.system("wpscan --url " + site + " --enumerate u" )
else:
	print("Hatalı Seçim Yaptınız...")
	
