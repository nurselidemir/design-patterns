from abc import ABC, abstractmethod

# Soyut Rapor sınıfı
class Rapor(ABC):
    @abstractmethod
    def hazirla(self):
        pass

# Temel Rapor Sınıfı
class TemelRapor(Rapor):
    def hazirla(self):
        return "Temel rapor hazır."

# Rapor Dekoratör (Decorator)
class RaporDecorator(Rapor):
    def __init__(self, rapor: Rapor):
        self._rapor = rapor

    def hazirla(self):
        return self._rapor.hazirla()

# Ekstra Bilgi Dekoratörü
class EkstraBilgiRapor(RaporDecorator):
    def hazirla(self):
        return f"{self._rapor.hazirla()} - Ekstra bilgiler eklendi."

# Stil Dekoratörü
class StilRapor(RaporDecorator):
    def hazirla(self):
        return f"{self._rapor.hazirla()} - Stil eklendi."

# Kullanım
temel_rapor = TemelRapor()
print(temel_rapor.hazirla())  # Temel rapor hazır.

ekstra_bilgi_rapor = EkstraBilgiRapor(temel_rapor)
print(ekstra_bilgi_rapor.hazirla())  # Temel rapor hazır. - Ekstra bilgiler eklendi.

stil_rapor = StilRapor(ekstra_bilgi_rapor)
print(stil_rapor.hazirla())  # Temel rapor hazır. - Ekstra bilgiler eklendi. - Stil eklendi.
