from abc import ABC, abstractmethod

# Observer (Gözlemci) sınıfı
class Observer(ABC):
    @abstractmethod
    def update(self, envanter_turu, veri):
        pass


# Envanter (Subject) sınıfı
class Envanter:
    def __init__(self):
        self._observers = []
    
    def add_observer(self, observer):
        self._observers.append(observer)
    
    def remove_observer(self, observer):
        self._observers.remove(observer)
    
    def notify(self, envanter_turu, veri):
        for observer in self._observers:
            observer.update(envanter_turu, veri)


# Tohum Envanteri
class TohumEnvanteri(Envanter):
    def __init__(self):
        super().__init__()
        self.tohumlar = {}

    def tohum_ekle(self, ad, miktar):
        if ad not in self.tohumlar:
            self.tohumlar[ad] = {"miktar": miktar, "kullanilan": 0}
        else:
            self.tohumlar[ad]["miktar"] += miktar
        self.notify("Tohum", {"ad": ad, "miktar": miktar, "işlem": "ekleme"})

    def tohum_kullan(self, ad, miktar):
        if ad in self.tohumlar and self.tohumlar[ad]["miktar"] >= miktar:
            self.tohumlar[ad]["miktar"] -= miktar
            self.tohumlar[ad]["kullanilan"] += miktar
            self.notify("Tohum", {"ad": ad, "miktar": miktar, "işlem": "kullanma"})
        else:
            print(f"Yeterli {ad} tohumu yok!")


# Alet Envanteri
class AletEnvanteri(Envanter):
    def __init__(self):
        super().__init__()
        self.aletler = {}

    def alet_ekle(self, ad):
        self.aletler[ad] = {"durum": "bende", "kime": None}
        self.notify("Alet", {"ad": ad, "işlem": "ekleme"})

    def alet_ver(self, ad, kime):
        if ad in self.aletler and self.aletler[ad]["durum"] == "bende":
            self.aletler[ad]["durum"] = "verildi"
            self.aletler[ad]["kime"] = kime
            self.notify("Alet", {"ad": ad, "kime": kime, "işlem": "verme"})
        else:
            print(f"{ad} ya mevcut değil ya da zaten verilmiş.")

    def alet_al(self, ad):
        if ad in self.aletler and self.aletler[ad]["durum"] == "verildi":
            self.aletler[ad]["durum"] = "bende"
            self.aletler[ad]["kime"] = None
            self.notify("Alet", {"ad": ad, "işlem": "geri alma"})
        else:
            print(f"{ad} zaten sende.")


# Gözlemci: Envanterdeki değişiklikleri izleyen sınıf
class EnvanterGozlemcisi(Observer):
    def update(self, envanter_turu, veri):
        print(f"\nGözlemci: {envanter_turu} envanterinde işlem yapıldı.")
        print(f"İşlem Türü: {veri['işlem']}, Ad: {veri['ad']}")
        if 'kime' in veri:
            print(f"Verilen Kişi: {veri['kime']}")
        if 'miktar' in veri:
            print(f"Eklenen/Kullanılan Miktar: {veri['miktar']}")


# Test fonksiyonu
def test_senaryosu():
    print(">>> Observer Tasarım Deseni Çiftlik Uygulaması Testi Başlatılıyor...\n")

    # Envanter nesneleri
    tohum_env = TohumEnvanteri()
    alet_env = AletEnvanteri()

    # Gözlemci nesnesi
    gozlemci = EnvanterGozlemcisi()

    # Gözlemciyi envanterlere ekle
    tohum_env.add_observer(gozlemci)
    alet_env.add_observer(gozlemci)

    # Tohum işlemleri
    tohum_env.tohum_ekle("bugday", 100)
    tohum_env.tohum_kullan("bugday", 30)

    # Alet işlemleri
    alet_env.alet_ekle("tırmık")
    alet_env.alet_ver("tırmık", "Ahmet")
    alet_env.alet_al("tırmık")


if __name__ == "__main__":
    test_senaryosu()
