# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'derskatılım.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(399, 442)
        self.tablo = QtWidgets.QTableWidget(Form)
        self.tablo.setGeometry(QtCore.QRect(0, 0, 401, 491))
        self.tablo.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tablo.setObjectName("tablo")
        self.tablo.setColumnCount(4)
        self.tablo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablo.setHorizontalHeaderItem(3, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Katıldığım Dersler"))
        item = self.tablo.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Katılım Tarihi"))
        item = self.tablo.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Ders Adı"))
        item = self.tablo.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Ders Öğretmeni"))
        item = self.tablo.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Ders Türü"))
