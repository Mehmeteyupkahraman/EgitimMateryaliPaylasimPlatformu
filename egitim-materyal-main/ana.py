from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from ana_ui import Ui_mainWindow
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtGui
from veritabani import Veritabani
from egitimmateryal import *
from derskatılım import DersKatilimSayfa
from ders import IcerikSayfa
from sorusor import SoruSorSayfa
from sorular import SorularSayfa

class AnaSayfa(QMainWindow):
    def __init__(self,uye) -> None:
        super().__init__()
        self.uye = uye
        self.anasayfa = Ui_mainWindow()
        self.anasayfa.setupUi(self)
        self.index = 0
        self.anasayfa.sonrakiButon.clicked.connect(self.sonraki)
        self.anasayfa.oncekiButon.clicked.connect(self.onceki)
        #self.anasayfa.biletButon.clicked.connect(self.oduncal)
        self.ders_liste_guncelle()
        self.dersguncelle()
        self.anasayfa.dersekatlbuton.clicked.connect(self.derskaydet)
        derskatilimsayfa = DersKatilimSayfa(uye)
        self.anasayfa.actionKt_ld_m_Dersler.triggered.connect(lambda: derskatilimsayfa.goster())
        self.iceriksayfa = IcerikSayfa()
        self.anasayfa.dersebaslabuton.clicked.connect(self.dersbasla)
        sorusor = SoruSorSayfa(uye)
        self.anasayfa.sorusorbuton.clicked.connect(lambda: sorusor.goster(self.dersler[self.index]))
        sorusayfasi = SorularSayfa(uye)
        self.anasayfa.actionSoru_Sayfas.triggered.connect(lambda: sorusayfasi.goster())

    def sonraki(self):
        self.index += 1
        if len(self.dersler) == self.index:
            self.index = 0
        self.dersguncelle()

    def onceki(self):
        self.index -= 1
        if self.index == -1:
            self.index = len(self.dersler)-1
        self.dersguncelle()

    def dersgoster(self, yeni_indeks):
        self.index = yeni_indeks
        self.dersguncelle()

    def dersguncelle(self):
        ders = self.dersler[self.index]

        self.anasayfa.foto.setPixmap(QtGui.QPixmap("fotoğraflar/" + ders.fotograf))
        self.anasayfa.dersadi.setText(ders.ad)
        self.anasayfa.ogretmenadi.setText(f'Öğretmen: {ders.ogretmen}')
        self.anasayfa.dersturu.setText(f'Ders Türü: {ders.turu}')
        self.anasayfa.konusu.setText(ders.ad + " Dersi Konusu:")
        self.anasayfa.aciklama.setText(ders.konu)        

        Veritabani.query("select * from ders_listem where kullanici_id = ? and ders_id = ?", (self.uye.id, ders.id))
        kayit = Veritabani.fetchone()
        if kayit is None:
            self.anasayfa.dersekatlbuton.setText("Derse Katıl")
        else:
            self.anasayfa.dersekatlbuton.setText("Dersten Ayrıl")  

    def ders_liste_guncelle(self):
        Veritabani.query("SELECT * FROM dersler")
        derssql = Veritabani.fetchall()
        dersler = []
        for ders in derssql:
            dersler.append(Ders(*ders))
        self.dersler = dersler

    def derskaydet(self):
        ders = self.dersler[self.index]
        yanit = QMessageBox.warning(self, "Ders", "İşlemi onaylıyor musunuz?", QMessageBox.Yes, QMessageBox.No)
        if yanit == QMessageBox.No:
            return
        butonyazi = self.anasayfa.dersekatlbuton.text()
        ders = self.dersler[self.index]
        if butonyazi == "Derse Katıl":
            self.uye.ders_ekle(ders)
            self.anasayfa.dersekatlbuton.setText("Dersten Ayrıl")
        else:
            self.uye.ders_sil(ders)
            self.anasayfa.dersekatlbuton.setText("Derse Katıl")
        QMessageBox.information(self,"Ders", "İşlem Tamamlandı", QMessageBox.Ok)

    def dersbasla(self):
        ders = self.dersler[self.index]
        Veritabani.query("select * from ders_listem where kullanici_id = ? and ders_id = ?", (self.uye.id, ders.id))
        kayit = Veritabani.fetchone()
        if kayit is None:
            QMessageBox.warning(self, "Ders", "Derse başlamak için önce derse katılmanız gerekiyor.", QMessageBox.Ok)
            return
        Veritabani.query('SELECT * FROM ders_icerik where ders_id=?',(ders.id,))
        icerik = Veritabani.fetchone()

        if icerik is None:
            QMessageBox.warning(self, "Ders", "Dersin içeriği yok.", QMessageBox.Ok)
        else:
            self.iceriksayfa.goster(ders)