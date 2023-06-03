from Insan import Insan

class Calisan(Insan):
    def __init__(self, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi, tesvik_primi):
        super().__init__(ad, soyad, yas, cinsiyet, uyruk)
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.uyruk = uyruk
        self.sektor = sektor
        self.tecrube = tecrube
        self.__maas = float(maas)
        self.yipranma_payi = float(yipranma_payi)
        self.tesvik_primi = float(tesvik_primi)

    def __convert_to_years(self, tecrube):
        years = tecrube // 12
        return years

    def set_sektor(self, sektor):
        if sektor in ["teknoloji", "muhasebe", "inşaat", "diğer"]:
            self.sektor = sektor
        else:
            raise ValueError("Geçersiz sektor değeri!")

    def get_sektor(self):
        return self.sektor

    def set_tecrube(self, tecrube):
        try:
            self.tecrube = int(tecrube)
        except ValueError:
            raise ValueError("Tecrube değeri tamsayı olmalıdır!")

    def get_tecrube(self):
        return self.tecrube

    def set_maas(self, maas):
        try:
            self.__maas = float(maas)
        except ValueError:
            raise ValueError("Maaş değeri ondalık sayı olmalıdır!")

    def get_maas(self):
        return self.__maas

    def set_yipranma_payi(self, yipranma_payi):
        try:
            self.__yipranma_payi = float(yipranma_payi)
        except ValueError:
            raise ValueError("Yıpranma payı değeri ondalık sayı olmalıdır!")

    def get_yipranma_payi(self):
        return self.yipranma_payi

    def get_tesvik_primi(self):
        return self.tesvik_primi

    def zam_hakki(self):
        if self.tecrube <= 0:
            return 0      # Yorum satırı: Tecrübe sıfırdan küçük veya eşitse zam yok.
        elif 2 <= self.tecrube <= 4 and self.__maas < 15000:
            return self.__maas * self.tecrube / 100   # Yorum satırı: Tecrübe 2-4 arasında ve maaş 15000'den düşükse zam miktarı maaşın %tecrube kadarı.
        elif self.tecrube > 4 and self.__maas < 25000:
            return self.__maas * self.tecrube / 200 # Yorum satırı: Tecrübe 4'ten büyük ve maaş 25000'den düşükse zam miktarı maaşın %tecrube/2 kadarı.
        else:
            return 0          #  Diğer durumlarda zam yok.

    def yeni_maas(self):
        self.maas = self.__maas + self.zam_hakki()
        return self.maas


    def __str__(self):

        return f"Ad: {self.ad}\nSoyad: {self.soyad}\nYaş: {self.yas}\nCinsiyet: {self.cinsiyet}\nUyruk: {self.uyruk}\nSektor: {self.sektor}\nTecrübe: {self.tecrube}\nMaaş: {self.__maas}\nYıpranma Payı: {self.yipranma_payi}\nTeşvik Primi: {self.tesvik_primi}"