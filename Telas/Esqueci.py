# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Esqueci.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EsqueciaSenha(object):
    def setupUi(self, EsqueciaSenha):
        EsqueciaSenha.setObjectName("EsqueciaSenha")
        EsqueciaSenha.resize(1354, 900)
        self.centralwidget = QtWidgets.QWidget(EsqueciaSenha)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 140, 381, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 450, 111, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(280, 330, 761, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        EsqueciaSenha.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EsqueciaSenha)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1354, 25))
        self.menubar.setObjectName("menubar")
        EsqueciaSenha.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EsqueciaSenha)
        self.statusbar.setObjectName("statusbar")
        EsqueciaSenha.setStatusBar(self.statusbar)

        self.retranslateUi(EsqueciaSenha)
        QtCore.QMetaObject.connectSlotsByName(EsqueciaSenha)

    def retranslateUi(self, EsqueciaSenha):
        _translate = QtCore.QCoreApplication.translate
        EsqueciaSenha.setWindowTitle(_translate("EsqueciaSenha", "MainWindow"))
        self.label.setText(_translate("EsqueciaSenha", "Esqueci a senha"))
        self.pushButton.setText(_translate("EsqueciaSenha", "Enviar"))
        self.label_2.setText(_translate("EsqueciaSenha", "EMAIL:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EsqueciaSenha = QtWidgets.QMainWindow()
    ui = Ui_EsqueciaSenha()
    ui.setupUi(EsqueciaSenha)
    EsqueciaSenha.show()
    sys.exit(app.exec_())

