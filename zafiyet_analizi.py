#!/usr/bin/env python

import os 
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet ZAAFIYET ANALIZI")
print("""
Zaafiyet Analizi Aracına Hoş Geldiniz...

""")

hedefip = input("Hedef İp Giriniz: ")
os.system("nikto -h " +hedefip)
