# Singleton Base Sınıfı
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Tohum Envanteri Singleton
class TohumEnvanteri(metaclass=SingletonMeta):
    def __init__(self):
        self.tohumlar = {}

    def tohum_ekle(self, ad, miktar):
        if ad not in self.tohumlar:
            self.tohumlar[ad] = {"miktar": miktar, "kullanilan": 0}
        else:
            self.tohumlar[ad]["miktar"] += miktar
        print(f"{miktar} adet {ad} tohumu eklendi.")

    def tohum_kullan(self, ad, miktar):
        if ad in self.tohumlar and self.tohumlar[ad]["miktar"] >= miktar:
            self.tohumlar[ad]["miktar"] -= miktar
            self.tohumlar[ad]["kullanilan"] += miktar
            print(f"{miktar} adet {ad} tohumu kullanıldı.")
        else:
            print(f"Yeterli {ad} tohumu yok!")

    def goster(self):
        print("\nTohum Envanteri:")
        for ad, veriler in self.tohumlar.items():
            print(f"- {ad}: {veriler['miktar']} mevcut, {veriler['kullanilan']} kullanıldı")

# Alet Envanteri Singleton
class AletEnvanteri(metaclass=SingletonMeta):
    def __init__(self):
        self.aletler = {}

    def alet_ekle(self, ad):
        self.aletler[ad] = {"durum": "bende", "kime": None}
        print(f"{ad} aleti eklendi.")

    def alet_ver(self, ad, kime):
        if ad in self.aletler and self.aletler[ad]["durum"] == "bende":
            self.aletler[ad]["durum"] = "verildi"
            self.aletler[ad]["kime"] = kime
            print(f"{ad} aleti {kime} kişisine verildi.")
        else:
            print(f"{ad} ya mevcut değil ya da zaten verilmiş.")

    def alet_al(self, ad):
        if ad in self.aletler and self.aletler[ad]["durum"] == "verildi":
            self.aletler[ad]["durum"] = "bende"
            self.aletler[ad]["kime"] = None
            print(f"{ad} aleti geri alındı.")
        else:
            print(f"{ad} zaten sende.")

    def goster(self):
        print("\nAlet Envanteri:")
        for ad, veriler in self.aletler.items():
            durum = f"{veriler['durum']} ({veriler['kime']})" if veriler['durum'] == "verildi" else "bende"
            print(f"- {ad}: {durum}")

# Test fonksiyonu
def test_senaryosu():
    print(">>> Singleton Çiftlik Uygulaması Testi Başlatılıyor...\n")

    tohum_env = TohumEnvanteri()
    alet_env = AletEnvanteri()

    # Tohum işlemleri
    tohum_env.tohum_ekle("bugday", 100)
    tohum_env.tohum_kullan("bugday", 30)
    tohum_env.tohum_ekle("misir", 50)
    tohum_env.tohum_kullan("misir", 10)
    tohum_env.goster()

    # Alet işlemleri
    alet_env.alet_ekle("tırmık")
    alet_env.alet_ekle("kürek")
    alet_env.alet_ver("kürek", "Ahmet")
    alet_env.alet_al("kürek")
    alet_env.goster()

    # Singleton testi
    print("\n>>> Singleton Testi")
    tohum_env2 = TohumEnvanteri()
    print("Aynı mı?", tohum_env is tohum_env2)

if __name__ == "__main__":
    test_senaryosu()