# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 609)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.telefonLine = QtWidgets.QLineEdit(Form)
        self.telefonLine.setGeometry(QtCore.QRect(150, 320, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.telefonLine.setFont(font)
        self.telefonLine.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.telefonLine.setStyleSheet("color:rgb(255, 255, 255)")
        self.telefonLine.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.telefonLine.setObjectName("telefonLine")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(150, 280, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 60, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(150, 200, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 360, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.kullaniciLine = QtWidgets.QLineEdit(Form)
        self.kullaniciLine.setGeometry(QtCore.QRect(150, 390, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.kullaniciLine.setFont(font)
        self.kullaniciLine.setStyleSheet("color:rgb(255, 255, 255)")
        self.kullaniciLine.setObjectName("kullaniciLine")
        self.kayitButon = QtWidgets.QPushButton(Form)
        self.kayitButon.setGeometry(QtCore.QRect(260, 510, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kayitButon.setFont(font)
        self.kayitButon.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(77, 77, 77);")
        self.kayitButon.setObjectName("kayitButon")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(150, 140, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 430, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.adLine = QtWidgets.QLineEdit(Form)
        self.adLine.setGeometry(QtCore.QRect(150, 170, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.adLine.setFont(font)
        self.adLine.setStyleSheet("color:rgb(255, 255, 255)")
        self.adLine.setObjectName("adLine")
        self.sifreLine = QtWidgets.QLineEdit(Form)
        self.sifreLine.setGeometry(QtCore.QRect(150, 460, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sifreLine.setFont(font)
        self.sifreLine.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.sifreLine.setStyleSheet("color: rgb(255, 255, 255);")
        self.sifreLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sifreLine.setObjectName("sifreLine")
        self.soyadLine = QtWidgets.QLineEdit(Form)
        self.soyadLine.setGeometry(QtCore.QRect(150, 240, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soyadLine.setFont(font)
        self.soyadLine.setStyleSheet("color:rgb(255, 255, 255)")
        self.soyadLine.setObjectName("soyadLine")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kayıt Ekranı"))
        self.label_6.setText(_translate("Form", "Telefon Numarası:"))
        self.label.setText(_translate("Form", "Kayıt Ol!"))
        self.label_5.setText(_translate("Form", "Soyadı:"))
        self.label_2.setText(_translate("Form", "Kullanıcı Adı:"))
        self.kayitButon.setText(_translate("Form", "Kayıt Ol"))
        self.label_4.setText(_translate("Form", "Adı:"))
        self.label_3.setText(_translate("Form", "Şifre:"))