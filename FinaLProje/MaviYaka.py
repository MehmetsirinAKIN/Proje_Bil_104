from Calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, ad, soyad, yas=None, cinsiyet=None, uyruk=None, sektor=None, tecrube=None, maas=None, yipranma_payi=None, tesvik_primi=None):
        super().__init__(ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi, tesvik_primi)

        self.sektor = sektor
        self.tecrube = tecrube
        self.maas = float(maas)
        self.yipranma_payi = float(yipranma_payi)
        self.tesvik_primi = float(tesvik_primi)

    def set_tecrube(self, tecrube):
        try:
            self.__tecrube = int(tecrube)
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
        return self.maas

    def set_yipranma_payi(self, yipranma_payi):
        try:
            self.__yipranma_payi = float(yipranma_payi)
        except ValueError:
            raise ValueError("Yıpranma payı değeri ondalık sayı olmalıdır!")

    def get_yipranma_payi(self):
        return self.yipranma_payi

    def zam_hakki(self):
        tecrube = self.get_tecrube()
        maas = self.get_maas()
        yipranma_payi= self.get_yipranma_payi()

        if tecrube < 2:
            return maas
        elif 2 <= tecrube <= 4 and maas < 15000:
            zam_orani = (maas % tecrube) / 2 + yipranma_payi * 10
        elif tecrube > 4 and maas < 25000:
            zam_orani = (maas % tecrube) / 3 + yipranma_payi * 10
        else:
            zam_orani = 0

        yeni_maas = maas + zam_orani
        return yeni_maas

    def __str__(self):
        yeni_maas = self.get_maas() + self.zam_hakki()
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nYaş: {self.get_yas()}\nCinsiyet: {self.get_cinsiyet()}\nUyruk: {self.get_uyruk()}\nSektor: {self.get_sektor()}\nTecrübe: {self.get_tecrube()}\nMaaş: {self.get_maas()}\nYıpranma Payı: {self.get_yipranma_payi()}\nTeşvik Primi: {self.tesvik_primi}"