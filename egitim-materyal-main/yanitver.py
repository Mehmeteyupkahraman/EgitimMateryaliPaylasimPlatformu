from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QMessageBox
from PyQt5 import QtCore
from yanitver_ui import Ui_MainWindow
from veritabani import Veritabani
from egitimmateryal import Ders

class OgretmenSayfa(QMainWindow):
    def __init__(self,ogretmen) -> None:
        super().__init__()
        self.ogretmen = ogretmen
        self.anasayfa = Ui_MainWindow()
        self.anasayfa.setupUi(self)
        self.anasayfa.yorumYapButon.clicked.connect(self.yanitver)
        
        tablo = self.anasayfa.tablo
        tablo.setRowCount(0)
        Veritabani.query('SELECT id, ders_id, soru FROM sorular WHERE yanit is null')
        sorularsql = Veritabani.fetchall()
        self.sorular = sorularsql

        if sorularsql is None:
            return
        
        tablo.setRowCount(len(sorularsql))
        satir = 0
        tablo.setColumnWidth(0, 100)
        tablo.setColumnWidth(1, 350)

        for id, ders_id, soru in sorularsql:
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

    def yanitver(self):
        index = self.anasayfa.tablo.currentRow()
        if (index < 0):
            return
        soru = self.sorular[index]
        yanittext = self.anasayfa.yanitText.toPlainText()

        if not yanittext:
            QMessageBox.warning(self, "Ders", "Lütfen geçerli bir yanıt girin.", QMessageBox.Ok)
            return
    
        yanit = QMessageBox.warning(self, "Ders", "Yanıt verme işlemini onaylıyor musunuz?", QMessageBox.Yes, QMessageBox.No)
        if yanit == QMessageBox.No:
            return
        
        Ders.soruya_yanit_ver(soru[0], yanittext)
        self.anasayfa.tablo.removeRow(index)

        QMessageBox.information(self, "Ders", "Yanıt verildi.", QMessageBox.Ok)
