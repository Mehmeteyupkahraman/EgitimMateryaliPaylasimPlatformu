# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sorular.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(476, 366)
        self.tablo = QtWidgets.QTableWidget(Form)
        self.tablo.setGeometry(QtCore.QRect(0, 0, 471, 161))
        self.tablo.setObjectName("tablo")
        self.tablo.setColumnCount(2)
        self.tablo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablo.setHorizontalHeaderItem(1, item)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 190, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.yanitlabel = QtWidgets.QLabel(Form)
        self.yanitlabel.setGeometry(QtCore.QRect(30, 220, 421, 121))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.yanitlabel.setFont(font)
        self.yanitlabel.setScaledContents(True)
        self.yanitlabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.yanitlabel.setWordWrap(True)
        self.yanitlabel.setObjectName("yanitlabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sorular"))
        item = self.tablo.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Ders"))
        item = self.tablo.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Soru"))
        self.label.setText(_translate("Form", "Yanıt:"))
        self.yanitlabel.setText(_translate("Form", "Yanıt Yok"))
