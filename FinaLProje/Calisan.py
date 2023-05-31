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

    

    def zam_hakki(self):
        if self.tecrube <= 0:
            return 0
        elif 2 <= self.tecrube <= 4 and self.__maas < 15000:
            return self.__maas * self.tecrube / 100
        elif self.tecrube > 4 and self.__maas < 25000:
            return self.__maas * self.tecrube / 200
        else:
            return 0

    def yeni_maas(self):
        self.maas = self.__maas + self.zam_hakki()
        return self.maas


    def __str__(self):

        return f"Ad: {self.ad}\nSoyad: {self.soyad}\nYaş: {self.yas}\nCinsiyet: {self.cinsiyet}\nUyruk: {self.uyruk}\nSektor: {self.sektor}\nTecrübe: {self.tecrube}\nMaaş: {self.__maas}\nYıpranma Payı: {self.yipranma_payi}\nTeşvik Primi: {self.tesvik_primi}"