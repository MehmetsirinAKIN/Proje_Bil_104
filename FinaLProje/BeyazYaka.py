from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi, tesvik_primi):
        super().__init__(ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi, tesvik_primi)

        self.sektor = sektor
        self.tecrube = tecrube
        self.maas = float(maas)
        self.yipranma_payi = float(yipranma_payi)
        self.tesvik_primi = float(tesvik_primi)

    def set_sektor(self, sektor):
        self.sektor = sektor

    def get_sektor(self):
        return self.sektor

    def set_tecrube(self, tecrube):
        self.tecrube = tecrube

    def get_tecrube(self):
        return self.tecrube

    def set_maas(self, maas):
        self.maas = float(maas)

    def get_maas(self):
        return self.maas

    def set_yipranma_payi(self, yipranma_payi):
        try:
            self.yipranma_payi = float(yipranma_payi)
        except ValueError:
            raise ValueError("Yıpranma payı değeri ondalık sayı olmalıdır!")

    def get_yipranma_payi(self):
        return self.yipranma_payi

    def set_tesvik_primi(self, tesvik_primi):
        self.tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.tesvik_primi

    def zam_hakki(self):
        if self.get_tecrube() <= 0:
            return 0
        else:
            return self.get_maas() * self.get_tecrube() / 100

    def __str__(self):
        yeni_maas = self.get_maas() + self.zam_hakki()
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()} ay\nYeni Maaş: {yeni_maas}"