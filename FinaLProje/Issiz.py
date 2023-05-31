from Insan import Insan

class Issiz(Insan):
    def __init__(self, ad, soyad, yas=None, cinsiyet=None, uyruk=None, tecrube=None, tc_no=None):
        super().__init__(ad, soyad, yas, cinsiyet, uyruk)
        self.ad = ad
        self.soyad = soyad
        self.tecrube = tecrube
        self.tc_no = tc_no

    def set_tc_no(self, tc_no):
        self.tc_no = tc_no

    def get_tc_no(self):
        return self.tc_no

    def set_tecrube(self, tecrube):
        self.tecrube = tecrube

    def get_tecrube(self):
        return self.tecrube

    def statu_bul(self):
        etkiler = {"mavi yaka": 0.2, "beyaz yaka": 0.35, "yönetici": 0.45}
        max_etki = max(etkiler.values())
        uygun_statu = [statu for statu, etki in etkiler.items() if etki == max_etki]
        return uygun_statu[0]

    def __str__(self):
        return f"Ad: {self.ad}\nSoyad: {self.soyad}\nEn Uygun Statü: {self.statu_bul()}"