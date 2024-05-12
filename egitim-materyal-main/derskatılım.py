from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from derskatılım_ui import Ui_Form
from PyQt5 import QtCore
from veritabani import Veritabani
from egitimmateryal import Ders
from datetime import datetime

class DersKatilimSayfa(QWidget):
    def __init__(self, kullanici) -> None:
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.kullanici = kullanici

    def goster(self):
        tablo = self.ui.tablo
        tablo.setRowCount(0)
        Veritabani.query('SELECT ders_id,katilmatarih FROM ders_listem WHERE kullanici_id = ?', (self.kullanici.id,))
        derslersql = Veritabani.fetchall()
        self.show()

        if derslersql is None:
            return

        tablo.setRowCount(len(derslersql))
        satir = 0
        tablo.setColumnWidth(0, 80)
        tablo.setColumnWidth(1, 105)
        tablo.setColumnWidth(2, 105)
        tablo.setColumnWidth(3, 90)

        for dersid,katilmatarih in derslersql:
            Veritabani.query("SELECT * FROM dersler WHERE id = ?", (dersid,))
            ders_sql = Veritabani.fetchone()
            ders = Ders(*ders_sql)

            izleme_tarihi_cell = QTableWidgetItem(str(datetime.strptime(katilmatarih, "%Y-%m-%d").strftime("%d.%m.%Y")))
            ders_ad_cell = QTableWidgetItem(ders.ad)
            ders_ogretmen_cell = QTableWidgetItem(ders.ogretmen)
            ders_tur_cell = QTableWidgetItem(ders.turu)
            # Hepsinin yazısını ortala
            ders_ad_cell.setTextAlignment(QtCore.Qt.AlignCenter)
            izleme_tarihi_cell.setTextAlignment(QtCore.Qt.AlignCenter)
            ders_ogretmen_cell.setTextAlignment(QtCore.Qt.AlignCenter)
            ders_tur_cell.setTextAlignment(QtCore.Qt.AlignCenter)

            tablo.setItem(satir, 0, izleme_tarihi_cell)
            tablo.setItem(satir, 1, ders_ad_cell)
            tablo.setItem(satir, 2, ders_ogretmen_cell)
            tablo.setItem(satir, 3, ders_tur_cell)
            satir += 1