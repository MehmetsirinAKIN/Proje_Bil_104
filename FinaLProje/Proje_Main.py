
import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

# Insan nesnesi oluşturma
try:
    insan1 = Insan("Ömer Asaf", "AKIN")
    insan1.set_tc_no("1234567890")
    insan1.set_yas(24)
    insan1.set_cinsiyet("Erkek")
    insan1.set_uyruk("Türk")

    insan2 = Insan("İbrahim", "Yılmaz")
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
    issiz1 = Issiz("Emin", "Kaynar", 35, "Erkek", "Türk", 5, "13579246805")
    issiz2 = Issiz("Zehra", "Benice", 25, "Kadın", "Türk", 3, "09876543241")
    issiz3 = Issiz("Mehmet", "Şirin", 40, "Erkek", "Türk", 4, "98765432510")

    print("\nİşsiz Bilgileri:")
    print(issiz1)
    print(issiz2)
    print(issiz3)
except ValueError as ve:
    print(f"Hata: {ve}")

# Calisan nesnesi oluşturma
try:

    calisan1 = Calisan("Emin", "Kaynar", 35, "Erkek", "Türk", "teknoloji", 3, 5000, 1.5, 2415)
    calisan1.set_tc_no("13579246807")

    calisan2 = Calisan("Zehra", "Benice", 25, "Kadın", "Türk", "muhasebe", 1, 10000, 2.4, 1457)
    calisan2.set_tc_no("19876543214")

    calisan3 = Calisan("Mehmet", "Şirin", 40, "Erkek", "Türk", "inşaat", 9, 20000, 1.9, 850)
    calisan3.set_tc_no("98765432105")

    print("\nÇalışan Bilgileri:")
    print(calisan1)
    print(calisan2)
    print(calisan3)
except ValueError as ve:
    print(f"Hata: {ve}")

# MaviYaka nesnesi oluşturma
try:
    mavi_yaka1 = MaviYaka("Kerem", "Salkım", 35, "Erkek", "Türk", "teknoloji", 1, 5000, 0.2,1965)
    mavi_yaka1.set_tc_no("87456254978")

    mavi_yaka2 = MaviYaka("Hatice", "Güngörmez", 25, "Kadın", "Türk", "muhasebe", 5, 10000, 0.5, 500)
    mavi_yaka2.set_tc_no("12324562138")

    mavi_yaka3 = MaviYaka("Yasin", "Güngörmez", 40, "Erkek", "Türk", "inşaat", 3, 20000, 0.2, 600)
    mavi_yaka3.set_tc_no("21065490756")
    print("  ")
    print("Mavi Yaka Bilgileri:")
    print(mavi_yaka1)
    print(mavi_yaka2)
    print(mavi_yaka3)
except ValueError as ve:
    print(f"Hata: {ve}")

# BeyazYaka nesnesi oluşturma
try:
    beyaz_yaka1 = BeyazYaka("Ahmet", "Kara", 35, "Erkek", "Türk", "teknoloji", 1.5, 5700, 2.1, 500)
    beyaz_yaka1.set_tc_no("12475259445")

    beyaz_yaka2 = BeyazYaka("Ayşe", "Yılmaz", 25, "Kadın", "Türk", "muhasebe", 4, 10200, 1.6, 2500)
    beyaz_yaka2.set_tc_no("21457896334")

    beyaz_yaka3 = BeyazYaka("Mehmet", "Sarı", 40, "Erkek", "Türk", "inşaat", 7, 21070, 2.05, 500)
    beyaz_yaka3.set_tc_no("78624530114")

    print("\nBeyaz Yaka Bilgileri:")
    print(beyaz_yaka1)
    print(beyaz_yaka2)
    print(beyaz_yaka3)
except ValueError as ve:
    print(f"Hata: {ve}")

# DataFrame oluşturma
data = {
    "nesne_degeri": ["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
    "tc_no": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(), mavi_yaka3.get_tc_no(), beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()],
    "ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), mavi_yaka1.get_ad(), mavi_yaka2.get_ad(), mavi_yaka3.get_ad(), beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],
    "soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(), mavi_yaka3.get_soyad(), beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()],
    "yas": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), mavi_yaka1.get_yas(), mavi_yaka2.get_yas(), mavi_yaka3.get_yas(), beyaz_yaka1.get_yas(), beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()],
    "cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(), mavi_yaka3.get_cinsiyet(), beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka3.get_cinsiyet()],
    "uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), mavi_yaka1.get_uyruk(), mavi_yaka2.get_uyruk(), mavi_yaka3.get_uyruk(), beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()],
    "sektor": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), mavi_yaka1.get_sektor(), mavi_yaka2.get_sektor(), mavi_yaka3.get_sektor(), beyaz_yaka1.get_sektor(), beyaz_yaka2.get_sektor(), beyaz_yaka3.get_sektor()],
    "tecrube": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), mavi_yaka1.get_tecrube(), mavi_yaka2.get_tecrube(), mavi_yaka3.get_tecrube(), beyaz_yaka1.get_tecrube(), beyaz_yaka2.get_tecrube(), beyaz_yaka3.get_tecrube()],
    "maas": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), mavi_yaka1.get_maas(), mavi_yaka2.get_maas(), mavi_yaka3.get_maas(), beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()],
    "yipranma_payi": [calisan1.get_yipranma_payi(), calisan2.get_yipranma_payi(), calisan3.get_yipranma_payi(), mavi_yaka1.get_yipranma_payi(), mavi_yaka2.get_yipranma_payi(), mavi_yaka3.get_yipranma_payi(), beyaz_yaka1.get_yipranma_payi(), beyaz_yaka2.get_yipranma_payi(), beyaz_yaka3.get_yipranma_payi()],
    "tesvik_primi": [calisan1.get_tesvik_primi(), calisan2.get_tesvik_primi(), calisan3.get_tesvik_primi(), mavi_yaka1.get_tesvik_primi(), mavi_yaka2.get_tesvik_primi(), mavi_yaka3.get_tesvik_primi(), beyaz_yaka1.get_tesvik_primi(), beyaz_yaka2.get_tesvik_primi(), beyaz_yaka3.get_tesvik_primi()],
    "yeni_maas": [calisan1.yeni_maas(), calisan2.yeni_maas(), calisan3.yeni_maas(), mavi_yaka1.yeni_maas(), mavi_yaka2.yeni_maas(), mavi_yaka3.yeni_maas(), beyaz_yaka1.yeni_maas(), beyaz_yaka2.yeni_maas(), beyaz_yaka3.yeni_maas()]
}

df = pd.DataFrame(data)

# a) Boş değerleri 0 olarak ayarlama
df = df.fillna(0)

# b) Gruplama ve ortalama hesaplama
gruplu_tecrube_maas = df.groupby(["nesne_degeri"])[["tecrube", "maas"]].mean()
print("\nGruplanmış Tecrübe ve Yeni Maaş Ortalamaları:")
print(gruplu_tecrube_maas)

# c) Maaşı 15000 TL üzerinde olanların sayısı
maas_ust_sinir = 15000
ust_siniri_gecenler = df[df["maas"] > maas_ust_sinir]
ust_siniri_gecenler_sayisi = len(ust_siniri_gecenler)
print("\n15000 TL üzerinde maaşı olanların sayısı:", ust_siniri_gecenler_sayisi)

# d) Yeni maaşa göre küçükten büyüğe sıralama
df_siralama = df.sort_values(by="yeni_maas")
print("\nYeni Maaşa Göre Sıralama:")
print(df_siralama)

# e) Tecrübesi 3 seneden fazla olan Beyaz Yakalıları bulma
tecrube_siniri = 3
beyaz_yaka_tecrube = df[(df["nesne_degeri"] == "Beyaz Yaka") & (df["tecrube"] > tecrube_siniri)]
print("\nTecrübesi 3 seneden fazla olan Beyaz Yakalılar:")
print(beyaz_yaka_tecrube)

# f) Yeni maaşı 10000 TL üzerinde olanların 2-5 satırlarını seçme
maas_siniri = 10000
ust_siniri_gecenler_2_5 = df[(df["yeni_maas"] > maas_siniri)].iloc[2:5, [1, 9]]
print("\nYeni maaşı 10000 TL üzerinde olanların 2-5 satırları:")
print(ust_siniri_gecenler_2_5)

# g) Ad, soyad, sektör ve yeni maaş içeren yeni DataFrame
yeni_df = df[["ad", "soyad", "sektor", "yeni_maas"]]
print("\nYeni DataFrame:")
print(yeni_df)
#  h) Excel'e yazma
df.to_excel("calisanlar.xlsx", index=False)

# # # i) CSV'ye yazma
df.to_csv("calisanlar.csv", index=False)
# #
# j) Dictionary'e dönüştürme
# df_dict = df.to_dict(orient="records")

# k) İsimlere göre filtreleme
isim_filtre = df[df["ad"].str.startswith("A")]
print("\nA harfi ile başlayan isimler:")
print(isim_filtre)