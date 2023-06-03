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
        tecrube = self.get_tecrube()
        maas = self.get_maas()
        tesvik_primi = self.get_tesvik_primi()

        if tecrube < 2:
            return maas  # Yorum satırı: Tecrübe 2'den küçükse zam yok.
        elif 2 <= tecrube <= 4 and maas < 15000:
            zam_miktari = (maas % tecrube) * 5 + tesvik_primi
            # Yorum satırı: Tecrübe 2-4 arasında ve maaş 15000'den düşükse zam miktarı (maas%tecrube)*5 + teşvik_primi.
        elif tecrube > 4 and maas < 25000:
            zam_miktari = (maas % tecrube) * 4 + tesvik_primi
            # Yorum satırı: Tecrübe 4'ten büyük ve maaş 25000'den düşükse zam miktarı (maas%tecrube)*4 + teşvik_primi.
        else:
            zam_miktari = 0
            # Yorum satırı: Diğer durumlarda zam yok.

        yeni_maas = maas + zam_miktari
        return yeni_maas

    def __str__(self):
        yeni_maas = self.get_maas() + self.zam_hakki()
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()} yıl\nYeni Maaş: {yeni_maas}"