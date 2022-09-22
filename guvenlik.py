#!/usr/bin/env python

import os 
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet GUVENLIK DUVARI TESPITI")
print("""
Güvenlik Duvarı Tespit Etme Aracına Hoş Geldiniz...

""")

site = input("Site Adresini Giriniz: ")
os.system("wafw00f "+ site)
