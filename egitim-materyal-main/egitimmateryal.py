from veritabani import Veritabani

class Kullanici:
    def __init__(self, id, kullaniciadi, sifre, ad, soyad, telefon, tur):
        self.id = id
        self.kullaniciadi = kullaniciadi
        self.sifre = sifre
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon
        self.tur = tur

    @staticmethod
    def kayitol(kullaniciadi, sifre, ad, soyad, telefon):
        Veritabani.query("INSERT INTO kullanicilar (kullaniciadi, sifre, ad, soyad, telefon) VALUES (?, ?, ?, ?, ?)", (kullaniciadi, sifre, ad, soyad, telefon))

    def ders_ekle(self, ders):
        Veritabani.query("INSERT INTO ders_listem (kullanici_id, ders_id, katilmatarih) VALUES (?, ?, date('now'))", (self.id, ders.id))

    def ders_sil(self, ders):
        Veritabani.query("DELETE FROM ders_listem WHERE kullanici_id = ? and ders_id = ?", (self.id, ders.id))

class Ders:
    def __init__ (self, id, ders_adi, ogretmen_adi, ders_turu, konu, fotograf):
        self.id = id
        self.ad = ders_adi
        self.ogretmen = ogretmen_adi
        self.turu = ders_turu
        self.konu = konu
        self.fotograf = fotograf

    def soru_sor(self, uye, soru):
        Veritabani.query("INSERT INTO sorular (kullanici_id, ders_id, soru) VALUES (?, ?, ?)", (uye.id, self.id, soru))
    
    @staticmethod
    def soruya_yanit_ver(soruid, yanit):
        Veritabani.query("UPDATE sorular SET yanit = ? WHERE id = ?", (yanit, soruid))


    
class Icerik:
    def __init__(self, id, dersid, sayfa, icerik):
        self.id = id
        self.dersid = dersid
        self.sayfa = sayfa
        self.icerik = icerik