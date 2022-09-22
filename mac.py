#!/usr/bin/env python

import os 
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MAC DEGISTIRME")
print("""
MAC Adresi Değiştirme Aracına Hoş  Geldiniz :)

1) MAC Adresini Random Belirle
2) MAC Adresini Elle Belirle
3) MAC Adresini Orjinale Döndür

""")

islemno = input("İşlem Numarasını Girin: ")

if(islemno == "1"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
	print(" \033[92mİşlem Başarılı ")
elif(islemno == "2"):
	mac = input ("Yeni MAC Adresini Girin: ")
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac " + mac + " eth0")
	os.system("ifconfig eth0 up")
	print(" \033[92mİşlem Başarılı ")
elif(islemno == "3"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth0 up")
	print(" \033[92mİşlem Başarılı ")
else:
	print(" Hatalı Seçim Yaptınız... ")
	os.system("python3 mac.py")
