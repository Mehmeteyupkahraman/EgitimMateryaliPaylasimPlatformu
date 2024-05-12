from PyQt5.QtWidgets import QWidget, QMessageBox
from sorusor_ui import Ui_Form

class SoruSorSayfa(QWidget):
    def __init__(self, uye) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.uye = uye
        self.form.sorbuton.clicked.connect(self.sor)

    def goster(self, ders):
        self.ders = ders
        self.form.label.setText(ders.ad + " Dersi")
        self.show()

    def sor(self):
        yanit = QMessageBox.warning(self, "Ders", "Soru sorma işlemini onaylıyor musunuz?", QMessageBox.Yes, QMessageBox.No)
        if yanit == QMessageBox.No:
            return
        
        soru = self.form.sorutext.toPlainText()
        self.ders.soru_sor(self.uye, soru)

        QMessageBox.information(self, "Ders", "Soru soruldu.", QMessageBox.Ok)
        self.close()