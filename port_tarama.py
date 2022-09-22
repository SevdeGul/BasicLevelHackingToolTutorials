#!/usr/bin/env python

import os 
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")
print("""
Port Tarama Aracına Hoş  Geldiniz :)

1)Hızlı Tarama
2)Servis ve Versiyon Bilgisi
3)İşletim Sistemi Bilgisi

""")

islemno = input ("İşlem Numarasını Giriniz: ")

if(islemno == "1"):
	hedefip = input("Hedef İp Giriniz: ")
	os.system("nmap " +hedefip)
elif(islemno == "2"):
	hedefip = input("Hedef İp Giriniz: ")
	os.system("nmap -sS -sV " + hedefip )
elif(islemno == "3"):
	hedefip = input("Hedef İp Giriniz: ")
	os.system("nmap -O " + hedefip )
else:
	print("Hatalı Seçim Yaptınız...")


