from abc import ABC, abstractmethod

# Strateji (Strategy) sınıfı
class IEnvanterIslemStratejisi(ABC):
    @abstractmethod
    def islem_yap(self, envanter, ad, miktar=None):
        pass


# Tohum ekleme stratejisi
class TohumEklemeStratejisi(IEnvanterIslemStratejisi):
    def islem_yap(self, envanter, ad, miktar):
        envanter.tohum_ekle(ad, miktar)


# Tohum kullanma stratejisi
class TohumKullanmaStratejisi(IEnvanterIslemStratejisi):
    def islem_yap(self, envanter, ad, miktar):
        envanter.tohum_kullan(ad, miktar)


# Alet ekleme stratejisi
class AletEklemeStratejisi(IEnvanterIslemStratejisi):
    def islem_yap(self, envanter, ad, miktar=None):
        envanter.alet_ekle(ad)


# Alet verme stratejisi
class AletVermeStratejisi(IEnvanterIslemStratejisi):
    def islem_yap(self, envanter, ad, miktar=None):
        envanter.alet_ver(ad, "Kullanıcı")  # Kullanıcıyı burada sabit alıyoruz.


# Tohum Envanteri
class TohumEnvanteri:
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


# Alet Envanteri
class AletEnvanteri:
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

    def goster(self):
        print("\nAlet Envanteri:")
        for ad, veriler in self.aletler.items():
            durum = f"{veriler['durum']} ({veriler['kime']})" if veriler['durum'] == "verildi" else "bende"
            print(f"- {ad}: {durum}")


# Envanterdeki işlem yönetimini sağlayan sınıf
class EnvanterIslemYonetimi:
    def __init__(self, strateji: IEnvanterIslemStratejisi):
        self.strateji = strateji

    def set_strateji(self, strateji: IEnvanterIslemStratejisi):
        self.strateji = strateji

    def islem_yap(self, envanter, ad, miktar=None):
        self.strateji.islem_yap(envanter, ad, miktar)


# Test fonksiyonu
def test_senaryosu():
    print(">>> Strategy Tasarım Deseni Çiftlik Uygulaması Testi Başlatılıyor...\n")

    # Envanter nesneleri
    tohum_env = TohumEnvanteri()
    alet_env = AletEnvanteri()

    # Strateji nesneleri
    tohum_ekleme_stratejisi = TohumEklemeStratejisi()
    tohum_kullanma_stratejisi = TohumKullanmaStratejisi()
    alet_ekleme_stratejisi = AletEklemeStratejisi()
    alet_verme_stratejisi = AletVermeStratejisi()

    # Envanter işlem yönetimi nesneleri
    tohum_islem_yonetimi = EnvanterIslemYonetimi(tohum_ekleme_stratejisi)
    alet_islem_yonetimi = EnvanterIslemYonetimi(alet_ekleme_stratejisi)

    # Tohum işlemleri
    tohum_islem_yonetimi.islem_yap(tohum_env, "bugday", 100)
    tohum_islem_yonetimi.set_strateji(tohum_kullanma_stratejisi)
    tohum_islem_yonetimi.islem_yap(tohum_env, "bugday", 30)

    # Alet işlemleri
    alet_islem_yonetimi.islem_yap(alet_env, "tırmık")
    alet_islem_yonetimi.set_strateji(alet_verme_stratejisi)
    alet_islem_yonetimi.islem_yap(alet_env, "tırmık")

    # Envanter gösterme
    tohum_env.goster()
    alet_env.goster()


if __name__ == "__main__":
    test_senaryosu()

