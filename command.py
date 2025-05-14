from abc import ABC, abstractmethod

# Komut Arayüzü
class Komut(ABC):
    @abstractmethod
    def execute(self):
        pass

# Gerçek Komut Sınıfları
class TVAç(Komut):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.ac()

class TVKapat(Komut):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.kapat()

class SesAç(Komut):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.ses_ac()

# Alıcı (Receiver)
class TV:
    def ac(self):
        print("TV açıldı.")
    
    def kapat(self):
        print("TV kapatıldı.")
    
    def ses_ac(self):
        print("Ses açıldı.")

# Komutları yönetmek için uzaktan kumanda (Invoker)
class UzaktanKumanda:
    def __init__(self):
        self.komutlar = []
    
    def komut_ekle(self, komut):
        self.komutlar.append(komut)
    
    def komutlari_calistir(self):
        for komut in self.komutlar:
            komut.execute()

# Kullanıcı işlemleri
tv = TV()

komut_ac = TVAç(tv)
komut_kapat = TVKapat(tv)
komut_ses_ac = SesAç(tv)

kumanda = UzaktanKumanda()

# Komutları uzaktan kumandaya ekle
kumanda.komut_ekle(komut_ac)
kumanda.komut_ekle(komut_ses_ac)
kumanda.komut_ekle(komut_kapat)

# Komutları çalıştır
kumanda.komutlari_calistir()
