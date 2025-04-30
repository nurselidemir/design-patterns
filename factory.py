from abc import ABC, abstractmethod
from datetime import datetime

# Soyut Rapor sınıfı
class Rapor(ABC):
    def __init__(self, tarih=None):
        self.tarih = tarih or datetime.now()

    @abstractmethod
    def yazdir(self):
        pass

# Ürün raporu sınıfı
class UrunRaporu(Rapor):
    def __init__(self, urun_adi, islem, miktar, birim, tarih=None):
        super().__init__(tarih)
        self.urun_adi = urun_adi
        self.islem = islem
        self.miktar = miktar
        self.birim = birim

    def yazdir(self):
        print(f"[ÜRÜN] {self.tarih.date()} - {self.urun_adi} {self.islem} - {self.miktar} {self.birim}")

# Hayvancılık raporu sınıfı
class HayvancilikRaporu(Rapor):
    def __init__(self, hayvan_turu, faaliyet, aciklama="", tarih=None):
        super().__init__(tarih)
        self.hayvan_turu = hayvan_turu
        self.faaliyet = faaliyet
        self.aciklama = aciklama

    def yazdir(self):
        print(f"[HAYVANCILIK] {self.tarih.date()} - {self.hayvan_turu} - {self.faaliyet} ({self.aciklama})")

# RaporFactory sınıfı
class RaporFactory:
    @staticmethod
    def rapor_olustur(rapor_tipi, **kwargs):
        if rapor_tipi == "urun":
            return UrunRaporu(
                urun_adi=kwargs.get("urun_adi"),
                islem=kwargs.get("islem"),
                miktar=kwargs.get("miktar"),
                birim=kwargs.get("birim"),
                tarih=kwargs.get("tarih")
            )
        elif rapor_tipi == "hayvancilik":
            return HayvancilikRaporu(
                hayvan_turu=kwargs.get("hayvan_turu"),
                faaliyet=kwargs.get("faaliyet"),
                aciklama=kwargs.get("aciklama"),
                tarih=kwargs.get("tarih")
            )
        else:
            raise ValueError(f"Bilinmeyen rapor tipi: {rapor_tipi}")

# Raporları yöneten sınıf
class RaporYonetici:
    def __init__(self):
        self.raporlar = []

    def rapor_ekle(self, rapor: Rapor):
        self.raporlar.append(rapor)

    def tum_raporlar(self):
        print("📄 Tüm Raporlar:")
        for rapor in self.raporlar:
            rapor.yazdir()

# Test fonksiyonu
def factory_test():
    factory = RaporFactory()
    yonetici = RaporYonetici()

    urun_raporu = factory.rapor_olustur(
        "urun",
        urun_adi="arpa",
        islem="ekim",
        miktar=150,
        birim="kg"
    )

    hayvan_raporu = factory.rapor_olustur(
        "hayvancilik",
        hayvan_turu="inek",
        faaliyet="sağım",
        aciklama="akşam sağımı yapıldı"
    )

    yonetici.rapor_ekle(urun_raporu)
    yonetici.rapor_ekle(hayvan_raporu)

    yonetici.tum_raporlar()

if __name__ == "__main__":
    factory_test()