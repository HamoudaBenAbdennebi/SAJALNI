# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\sajalni\sajalni-interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_appmain(object):
    def setupUi(self, appmain):
        appmain.setObjectName("appmain")
        appmain.resize(540, 319)
        appmain.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(appmain)
        self.centralwidget.setObjectName("centralwidget")
        self.IMEI = QtWidgets.QLineEdit(self.centralwidget)
        self.IMEI.setGeometry(QtCore.QRect(30, 30, 481, 71))
        self.IMEI.setStyleSheet("font: 26pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.IMEI.setMaxLength(15)
        self.IMEI.setObjectName("IMEI")
        self.NUMBER = QtWidgets.QLineEdit(self.centralwidget)
        self.NUMBER.setGeometry(QtCore.QRect(30, 110, 481, 71))
        self.NUMBER.setStyleSheet("font: 26pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.NUMBER.setMaxLength(8)
        self.NUMBER.setObjectName("NUMBER")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 190, 481, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verifier = QtWidgets.QPushButton(self.frame)
        self.verifier.setGeometry(QtCore.QRect(0, 0, 231, 71))
        self.verifier.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 18pt \"Arial\";")
        self.verifier.setObjectName("verifier")
        self.bloquer = QtWidgets.QPushButton(self.frame)
        self.bloquer.setGeometry(QtCore.QRect(250, 0, 231, 71))
        self.bloquer.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 18pt \"Arial\";")
        self.bloquer.setObjectName("bloquer")
        appmain.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(appmain)
        self.statusbar.setObjectName("statusbar")
        appmain.setStatusBar(self.statusbar)

        self.retranslateUi(appmain)
        QtCore.QMetaObject.connectSlotsByName(appmain)

    def retranslateUi(self, appmain):
        _translate = QtCore.QCoreApplication.translate
        appmain.setWindowTitle(_translate("appmain", "MainWindow"))
        self.IMEI.setPlaceholderText(_translate("appmain", " IMEI*"))
        self.NUMBER.setPlaceholderText(_translate("appmain", " NUMERO*"))
        self.verifier.setText(_translate("appmain", "vérifier"))
        self.bloquer.setText(_translate("appmain", "bloquer"))