# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Administrador.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TelaAdmin(object):
    def setupUi(self, TelaAdmin):
        TelaAdmin.setObjectName("TelaAdmin")
        TelaAdmin.resize(1266, 598)
        self.centralwidget = QtWidgets.QWidget(TelaAdmin)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 70, 1231, 821))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 110, 225, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.dateEdit = QtWidgets.QDateEdit(self.tab)
        self.dateEdit.setGeometry(QtCore.QRect(350, 370, 110, 27))
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 110, 591, 91))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(350, 220, 238, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(350, 520, 243, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(350, 260, 591, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_3.addWidget(self.lineEdit_4)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(350, 410, 591, 91))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_4.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_4.addWidget(self.lineEdit_6)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(526, 586, 141, 61))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(40, 70, 571, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(640, 70, 571, 291))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(175, 30, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(780, 30, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 390, 121, 61))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(115, 506, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(60, 590, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(170, 590, 291, 27))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.radioButton_5 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_5.setGeometry(QtCore.QRect(190, 640, 115, 22))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_6.setGeometry(QtCore.QRect(310, 640, 131, 22))
        self.radioButton_6.setObjectName("radioButton_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 696, 121, 41))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(550, 510, 331, 221))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.radioButton_7 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_7.setGeometry(QtCore.QRect(450, 290, 131, 22))
        self.radioButton_7.setObjectName("radioButton_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(310, 240, 291, 27))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_4.setGeometry(QtCore.QRect(690, 160, 331, 221))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 346, 171, 41))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(200, 240, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.radioButton_8 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_8.setGeometry(QtCore.QRect(330, 290, 115, 22))
        self.radioButton_8.setObjectName("radioButton_8")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(255, 156, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(386, 416, 161, 41))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-top-color: rgb(255, 0, 0);\n"
"background-color: rgb(204, 0, 0);")
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1130, 30, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setObjectName("pushButton_6")
        TelaAdmin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaAdmin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1266, 26))
        self.menubar.setObjectName("menubar")
        TelaAdmin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaAdmin)
        self.statusbar.setObjectName("statusbar")
        TelaAdmin.setStatusBar(self.statusbar)

        self.retranslateUi(TelaAdmin)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(TelaAdmin)

    def retranslateUi(self, TelaAdmin):
        _translate = QtCore.QCoreApplication.translate
        TelaAdmin.setWindowTitle(_translate("TelaAdmin", "MainWindow"))
        self.label_2.setText(_translate("TelaAdmin", "Nome"))
        self.label.setText(_translate("TelaAdmin", "CPF"))
        self.label_4.setText(_translate("TelaAdmin", "Sexo"))
        self.label_3.setText(_translate("TelaAdmin", "Endereco"))
        self.label_5.setText(_translate("TelaAdmin", "Email"))
        self.label_6.setText(_translate("TelaAdmin", "Data de Nascimento"))
        self.label_7.setText(_translate("TelaAdmin", "Usuário"))
        self.label_8.setText(_translate("TelaAdmin", "Senha"))
        self.label_9.setText(_translate("TelaAdmin", "Tipo de Funcionario"))
        self.dateEdit.setDisplayFormat(_translate("TelaAdmin", "dd/MM/yyyy"))
        self.radioButton.setText(_translate("TelaAdmin", "Masculino"))
        self.radioButton_2.setText(_translate("TelaAdmin", "Feminino"))
        self.radioButton_3.setText(_translate("TelaAdmin", "Funcionario"))
        self.radioButton_4.setText(_translate("TelaAdmin", "Administrador"))
        self.pushButton.setText(_translate("TelaAdmin", "Cadastrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("TelaAdmin", "Cadastrar um Funcionario"))
        self.label_10.setText(_translate("TelaAdmin", "Funcionarios"))
        self.label_11.setText(_translate("TelaAdmin", "Administradores"))
        self.pushButton_2.setText(_translate("TelaAdmin", "Listar"))
        self.label_12.setText(_translate("TelaAdmin", "Procurar um Funcionario"))
        self.label_13.setText(_translate("TelaAdmin", "CPF"))
        self.radioButton_5.setText(_translate("TelaAdmin", "Funcionario"))
        self.radioButton_6.setText(_translate("TelaAdmin", "Administrador"))
        self.pushButton_3.setText(_translate("TelaAdmin", "Buscar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("TelaAdmin", "Listar Funcionarios"))
        self.radioButton_7.setText(_translate("TelaAdmin", "Administrador"))
        self.pushButton_4.setText(_translate("TelaAdmin", "Buscar"))
        self.label_14.setText(_translate("TelaAdmin", "CPF"))
        self.radioButton_8.setText(_translate("TelaAdmin", "Funcionario"))
        self.label_15.setText(_translate("TelaAdmin", "Procurar o Funcionario"))
        self.pushButton_5.setText(_translate("TelaAdmin", "Demitir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("TelaAdmin", "Demitir um Funcionario"))
        self.pushButton_6.setText(_translate("TelaAdmin", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaAdmin = QtWidgets.QMainWindow()
    ui = Ui_TelaAdmin()
    ui.setupUi(TelaAdmin)
    TelaAdmin.show()
    sys.exit(app.exec_())
