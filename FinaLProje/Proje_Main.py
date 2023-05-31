
import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

# Insan nesnesi oluşturma
try:
    insan1 = Insan("Ali", "Demir")
    insan1.set_tc_no("1234567890")
    insan1.set_yas(30)
    insan1.set_cinsiyet("Erkek")
    insan1.set_uyruk("Türk")

    insan2 = Insan("Ayşe", "Yılmaz")
    insan2.set_tc_no("0987654321")
    insan2.set_yas(25)
    insan2.set_cinsiyet("Kadın")
    insan2.set_uyruk("Türk")

    print("İnsan Bilgileri:")
    print(insan1)
    print(insan2)
except ValueError as ve:
    print(f"Hata: {ve}")

# Issiz nesnesi oluşturma
try:
    issiz1 = Issiz("Ahmet", "Kara", 35, "Erkek", "Türk", 5, "1357924680")
    issiz2 = Issiz("Ayşe", "Yılmaz", 25, "Kadın", "Türk", 3, "0987654321")
    issiz3 = Issiz("Mehmet", "Sarı", 40, "Erkek", "Türk", 4, "9876543210")

    print("\nİşsiz Bilgileri:")
    print(issiz1)
    print(issiz2)
    print(issiz3)
except ValueError as ve:
    print(f"Hata: {ve}")

# Calisan nesnesi oluşturma
try:

    calisan1 = Calisan("Ahmet", "Kara", 35, "Erkek", "Türk", "teknoloji", 24, 5000, 1.5, 2415)
    calisan1.set_tc_no("1357924680")

    calisan2 = Calisan("Ayşe", "Yılmaz", 25, "Kadın", "Türk", "muhasebe", 48, 10000, 2.4, 1457)
    calisan2.set_tc_no("0987654321")

    calisan3 = Calisan("Mehmet", "Sarı", 40, "Erkek", "Türk", "inşaat", 60, 20000, 1.9, 850)
    calisan3.set_tc_no("9876543210")

    print("\nÇalışan Bilgileri:")
    print(calisan1)
    print(calisan2)
    print(calisan3)
except ValueError as ve:
    print(f"Hata: {ve}")

# MaviYaka nesnesi oluşturma
try:
    mavi_yaka1 = MaviYaka("Ahmet", "Kara", 35, "Erkek", "Türk", "teknoloji", 24, 5000, 0.2,1965)
    mavi_yaka1.set_tc_no("8745625478")

    mavi_yaka2 = MaviYaka("Ayşe", "Yılmaz", 25, "Kadın", "Türk", "muhasebe", 48, 10000, 0.5, 500)
    mavi_yaka2.set_tc_no("12324562138")

    mavi_yaka3 = MaviYaka("Mehmet", "Sarı", 40, "Erkek", "Türk", "inşaat", 60, 20000, 0.2, 600)
    mavi_yaka3.set_tc_no("21065490756")

    print("Mavi Yaka Bilgileri:")
    print(mavi_yaka1)
    print(mavi_yaka2)
    print(mavi_yaka3)
except ValueError as ve:
    print(f"Hata: {ve}")

# BeyazYaka nesnesi oluşturma
try:
    beyaz_yaka1 = BeyazYaka("Ahmet", "Kara", 35, "Erkek", "Türk", "teknoloji", 24, 5000, 2.1, 500)
    beyaz_yaka1.set_tc_no("1247525445")

    beyaz_yaka2 = BeyazYaka("Ayşe", "Yılmaz", 25, "Kadın", "Türk", "muhasebe", 48, 10000, 1.6, 2500)
    beyaz_yaka2.set_tc_no("21457896334")

    beyaz_yaka3 = BeyazYaka("Mehmet", "Sarı", 40, "Erkek", "Türk", "inşaat", 60, 20000, 2.05, 500)
    beyaz_yaka3.set_tc_no("78624530114")

    print("\nBeyaz Yaka Bilgileri:")
    print(beyaz_yaka1)
    print(beyaz_yaka2)
    print(beyaz_yaka3)
except ValueError as ve:
    print(f"Hata: {ve}")
