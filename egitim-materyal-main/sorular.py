from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from sorular_ui import Ui_Form
from PyQt5 import QtCore
from datetime import datetime
from veritabani import Veritabani
from egitimmateryal import Ders

class SorularSayfa(QWidget):
    def __init__(self, uye) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.uye = uye
        self.form.tablo.currentCellChanged.connect(self.yanitguncelle)

    def goster(self):
        self.tablo_guncelle()
        self.show()

        #tablo.resizeColumnsToContents()

    def yanitguncelle(self):
        index = self.form.tablo.currentRow()
        if (index < 0):
            return
        soru = self.sorular[index]
        if (soru[2] is None):
            self.form.yanitlabel.setText("Yanıt Yok")
        else:
            self.form.yanitlabel.setText(soru[2])


    def tablo_guncelle(self):
        tablo = self.form.tablo
        tablo.setRowCount(0)
        Veritabani.query('SELECT ders_id, soru, yanit FROM sorular WHERE kullanici_id = ?', (self.uye.id,))
        sorularsql = Veritabani.fetchall()
        self.sorular = sorularsql

        if sorularsql is None:
            return
        
        tablo.setRowCount(len(sorularsql))
        satir = 0
        tablo.setColumnWidth(0, 100)
        tablo.setColumnWidth(1, 350)

        for ders_id, soru, yanit in sorularsql:
            Veritabani.query("SELECT * FROM dersler WHERE id = ?", (ders_id,))
            derssql = Veritabani.fetchone()
            ders = Ders(*derssql)

            derscell = QTableWidgetItem(ders.ad)
            sorucell = QTableWidgetItem(soru)

            #Hepsinin yazısını ortala
            derscell.setTextAlignment(QtCore.Qt.AlignCenter)
            sorucell.setTextAlignment(QtCore.Qt.AlignCenter)

            tablo.setItem(satir, 0, derscell)
            tablo.setItem(satir, 1, sorucell)
            satir+=1