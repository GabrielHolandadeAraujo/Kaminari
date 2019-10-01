from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem
from Telas.Administrador import Ui_TelaAdmin
from Telas.CadastroUsuario import Ui_CadastroUsuario
from Telas.Esqueci import Ui_EsqueciaSenha
from Telas.Funcionario import Ui_Tela_Funcionario
from Telas.Login import Ui_Login
from Telas.Usuario import Ui_Usuario
import PyQt5
import sys
import os
from PyQt5.QtCore import pyqtSlot
import socket

class UI_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(1200, 900)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()

        self.tela_login = Ui_Login()
        self.tela_login.setupUi(self.stack0)

        self.tela_cadastro = Ui_CadastroUsuario()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_usuario = Ui_Usuario()
        self.tela_usuario.setupUi(self.stack2)

        self.tela_admin = Ui_TelaAdmin()
        self.tela_admin.setupUi(self.stack3)

        self.tela_func = Ui_Tela_Funcionario()
        self.tela_func.setupUi(self.stack4)

        self.tela_recup = Ui_EsqueciaSenha()
        self.tela_recup.setupUi(self.stack5)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)

class Main(QMainWindow, UI_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        #lembrar de zerar os campos
        self.tela_login.EsqueciButton.clicked.connect(self.esqueci)
        self.tela_login.LoginButton.clicked.connect(self.entrar)
        self.tela_login.CadButton.clicked.connect(self.criarConta)
        self.tela_cadastro.voltar.clicked.connect(self.voltaLog)
        self.tela_recup.voltar.clicked.connect(self.voltaLog)

        '''self.tela_inicio.botao_entrar.clicked.connect(self.entrar)
        self.tela_inicio.botao_criar_conta.clicked.connect(self.openCriarConta)

        self.tela_cadastro.botao_salvar.clicked.connect(self.criarConta)
        self.tela_cadastro.toolButton.clicked.connect(self.voltarInicio)

        self.tela_principal.cadastrar_novo_livro.clicked.connect(self.openCadastrarLivro)
        self.tela_principal.ver_acervo.clicked.connect(self.openAcervoLivro)
        self.tela_principal.sair.clicked.connect(self.voltarInicio)

        self.tela_cadastro_livro.botao_salvar_livro.clicked.connect(self.cadastrarLivro)
        self.tela_cadastro_livro.buttonVoltar.clicked.connect(self.voltarPrincipal)

        self.tela_acervo.sair.clicked.connect(self.entrar)'''

    def esqueci(self):
        self.QtStack.setCurrentIndex(5)

    def voltaLog(self):
        self.QtStack.setCurrentIndex(0)
    
    def entrar(self):
        enviar = 'LGIN'
        recebe = ''
        if self.tela_login.radioButton.isChecked():
            enviar = enviar + ',US' + ',' + self.tela_login.lineEdit.text() +  ',' + self.tela_login.lineEdit_2.text()
            client_socket.send(menviar.encode())
            recebe = client_socket.recv(1024)
            if('T' in recebe.decode()):
                self.QtStack.setCurrentIndex(2)
            elif('Pass' in recebe.decode()):
                QtWidgets.QMessageBox.information('Senha Inválida!')
            elif('User' in recebe.decode()):
                QtWidgets.QMessageBox.information('Usuário Inválido!')
        elif self.tela_login.radioButton_2.isChecked():
            self.QtStack.setCurrentIndex(4)
        elif self.tela_login.radioButton_3.isChecked():
            self.QtStack.setCurrentIndex(3)
        else:
            QtWidgets.QMessageBox.information(None,'Erro','Selecione o tipo de conta')
        

    def openCriarConta(self):
        self.QtStack.setCurrentIndex(1)

    def voltarInicio(self):
        self.QtStack.setCurrentIndex(0)

    def criarConta(self):
        self.QtStack.setCurrentIndex(1)

    def openCadastrarLivro(self):
        self.QtStack.setCurrentIndex(3)

    def openAcervoLivro(self):
        self.QtStack.setCurrentIndex(4)

    def voltarPrincipal(self):
        self.QtStack.setCurrentIndex(2)

    def cadastrarLivro(self):
        self.QtStack.setCurrentIndex(2)

if __name__ == '__main__':
    ip = input('Digite o ip da concexão:')
    port = 7009
    addr = ((ip, port))
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(addr)
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
