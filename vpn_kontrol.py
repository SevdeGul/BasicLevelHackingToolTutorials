#!/usr/bin/env python

import os 

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VPN KONTROL")

print("""
VPN Kontrol Aracına Hoş  Geldiniz... :)

""")

hedefip = input("Hedep IP Girin: ")
os.system("ike-scan "+ hedefip )
