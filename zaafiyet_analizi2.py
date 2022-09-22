#!/usr/bin/env python

import os 
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet ZAAFIYET ANALIZI 2")
print("""
Zaafiyet Analizi 2 Aracına Hoş  Geldiniz... :)

""")

os.system("lynis audit system")

print("""

Açıklama Bölümü

""")
