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
        self.tela_cadastro.cadUsuario.clicked.connect(self.cadastrar)
        self.tela_usuario.pushButton_2.clicked.connect(self.voltaLog)
        self.tela_recup.pushButton.clicked.connect(self.enviaEmail)
        self.tela_usuario.calculaFrete.clicked.connect(self.calculaPreco)
        self.tela_func.pushButton_3.clicked.connect(self.voltaLog)
        self.tela_admin.pushButton_6.clicked.connect(self.voltaLog)

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
        self.tela_usuario.lineEdit.setText(''), self.tela_usuario.lineEdit_2.setText(''), self.tela_usuario.lineEdit_3.setText(''), self.tela_usuario.lineEdit_4.setText(''), self.tela_usuario.lineEdit_6.setText(''), self.tela_usuario.textBrowser.setText(''), self.tela_usuario.valorFrete.setText(''), self.tela_usuario.prodRastreado.setText('')
        self.tela_admin.lineEdit.setText(''), self.tela_admin.lineEdit_2.setText(''), self.tela_admin.lineEdit_3.setText(''), self.tela_admin.lineEdit_4.setText(''), self.tela_admin.lineEdit_5.setText(''), self.tela_admin.lineEdit_6.setText(''), self.tela_admin.lineEdit_7.setText(''), self.tela_admin.lineEdit_8.setText(''), self.tela_admin.textBrowser.setText(''), self.tela_admin.textBrowser_2.setText(''), self.tela_admin.textBrowser_3.setText(''), self.tela_admin.textBrowser_4.setText('')
        self.tela_func.lineEdit.setText(''), self.tela_func.lineEdit_2.setText(''), self.tela_func.lineEdit_3.setText(''), self.tela_func.lineEdit_4.setText(''), self.tela_func.lineEdit_5.setText(''), self.tela_func.lineEdit_6.setText(''), self.tela_func.lineEdit_7.setText(''), self.tela_func.lineEdit_8.setText(''), self.tela_func.lineEdit_9.setText(''), self.tela_func.lineEdit_20.setText(''), self.tela_func.lineEdit_21.setText(''), self.tela_func.textBrowser.setText(''), self.tela_func.textBrowser_2.setText(''), self.tela_func.Info_pacote.setText('')
        self.QtStack.setCurrentIndex(0)
    
    def calculaPreco(self):
        envia = ''
        recebe = ''
        peso, alt, comp, prof = self.tela_usuario.lineEdit_6.text(), self.tela_usuario.lineEdit_4.text(), self.tela_usuario.lineEdit.text(), self.tela_usuario.lineEdit_2.text()
        if(self.tela_usuario.radioButton.isChecked()):
            frag = 'Não'
        elif(self.tela_usuario.radioButton_2.isChecked()):
            frag = 'Sim'
        else:
            QtWidgets.QMessageBox.information(None,'Erro','O pacote é fragil?')
        if(self.tela_usuario.radioButton_3.isChecked()):
            tipo = 'Normal'
        elif(self.tela_usuario.radioButton_4.isChecked()):
            tipo = 'Expresso'
        else:
            QtWidgets.QMessageBox.information(None,'Erro','Selecione o tipo de entrega!')
        envia = 'PAC,CAL,{},{},{},{},{},{}'.format(peso, alt, comp, prof, frag, tipo)
        client_socket.send(envia.encode())
        recebe = client_socket.recv(1024)
        if('T' in recebe.decode()):
            valor = ''
            valor = recebe.decode()
            valor = valor.split(',')
            self.tela_usuario.valorFrete.setText('{} R$'.format(valor[1]))
        else:
            QtWidgets.QMessageBox.information(None,'Erro','Preencha todos os campos!')

    def enviaEmail(self):
        envia = 'Email' + ',' + self.tela_recup.lineEdit.text()
        if('@' in self.tela_recup.lineEdit.text() and '.' in self.tela_recup.lineEdit.text()):
            client_socket.send(envia.encode())
            QtWidgets.QMessageBox.information(None, 'Confirmação', 'A nova senha foi enviada para o email {}.'.format(self.tela_recup.lineEdit.text()))
            self.tela_recup.lineEdit.setText('')
            self.QtStack.setCurrentIndex(0)
        else:
            QtWidgets.QMessageBox.information(None, 'Erro', 'Digite um email válido.')

    def cadastrar(self):
        recebe = ''
        envia = ''
        nome, cpf, email, end, nasc, user, pas = self.tela_cadastro.lineEdit.text(), self.tela_cadastro.lineEdit_2.text(), self.tela_cadastro.lineEdit_4.text(), self.tela_cadastro.lineEdit_6.text(), self.tela_cadastro.lineEdit_5.text(), self.tela_cadastro.lineEdit_7.text(), self.tela_cadastro.lineEdit_8.text()
        if(self.tela_cadastro.radioButton.isChecked()):
            sexo = 'M'
        elif(self.tela_cadastro.radioButton_2.isChecked()):
            sexo = 'F'
        else:
            QtWidgets.QMessageBox.information(None,'Erro','Selecione o sexo!')
        #envia = 'CAD' + ',' + 'US' + ',' + nome + ',' + cpf + ',' + sexo + ',' + email + ',' + end + ',' + nasc + ',' + user + ',' + pas
        envia = 'CAD,US,{},{},{},{},{},{},{},{}'.format(nome, cpf, sexo, email, end, nasc, user, pas)
        client_socket.send(envia.encode())
        recebe = client_socket.recv(1024)
        if('T' in recebe.decode()):
            QtWidgets.QMessageBox.information(None,'Confirmação','Cadastrado realizado com sucesso!')
            self.tela_cadastro.lineEdit.setText(''), self.tela_cadastro.lineEdit_2.setText(''), self.tela_cadastro.lineEdit_4.setText(''), self.tela_cadastro.lineEdit_6.setText(''), self.tela_cadastro.lineEdit_5.setText(''), self.tela_cadastro.lineEdit_7.setText(''), self.tela_cadastro.lineEdit_8.setText('')
            self.QtStack.setCurrentIndex(0)
        elif('User' in recebe.decode()):
            if('Err' in recebe.decode()):
                QtWidgets.QMessageBox.information(None,'Erro','O tamanho mínimo do usuário é de 6 caracteres!')    
            else:  
                QtWidgets.QMessageBox.information(None,'Erro','Esse usuário já existe!')
        elif('CPF' in recebe.decode()):
            if('Err' in recebe.decode()):
                QtWidgets.QMessageBox.information(None, 'Erro', 'Digite um CPF válido!')
            else:
                QtWidgets.QMessageBox.information(None, 'Erro,', 'Esse CPF já está cadastrado!')
        else:
            QtWidgets.QMessageBox.information(None,'Erro','Preencha todos os campos!')


    def entrar(self):
        enviar = 'LGIN'
        recebe = ''
        if self.tela_login.radioButton.isChecked():
            enviar = enviar + ',US' + ',' + self.tela_login.lineEdit.text() +  ',' + self.tela_login.lineEdit_2.text()
            client_socket.send(enviar.encode())
            recebe = client_socket.recv(1024)
            if('T' in recebe.decode()):
                self.QtStack.setCurrentIndex(2)
                self.tela_login.lineEdit.setText(''), self.tela_login.lineEdit_2.setText('')
            elif('Pass' in recebe.decode()):
                QtWidgets.QMessageBox.information(None,'Erro','Senha Inválida!')
            elif('User' in recebe.decode()):
                QtWidgets.QMessageBox.information(None,'Erro','Usuário Inválido!')
        elif self.tela_login.radioButton_2.isChecked():
            enviar = enviar + ',FC' + ',' + self.tela_login.lineEdit.text() +  ',' + self.tela_login.lineEdit_2.text()
            client_socket.send(enviar.encode())
            recebe = client_socket.recv(1024)
            if('T' in recebe.decode()):
                self.QtStack.setCurrentIndex(4)
            elif('Pass' in recebe.decode()):
                QtWidgets.QMessageBox.information(None,'Erro','Senha Inválida!')
            elif('User' in recebe.decode()):
                QtWidgets.QMessageBox.information(None,'Erro','Usuário Inválido!')
        elif self.tela_login.radioButton_3.isChecked():
            enviar = enviar + ',AD' + ',' + self.tela_login.lineEdit.text() +  ',' + self.tela_login.lineEdit_2.text()
            client_socket.send(enviar.encode())
            recebe = client_socket.recv(1024)
            if('T' in recebe.decode()):
                self.QtStack.setCurrentIndex(3)
            elif('Pass' in recebe.decode()):
                QtWidgets.QMessageBox.information(None,'Erro','Senha Inválida!')
            elif('User' in recebe.decode()):
                QtWidgets.QMessageBox.information(None,'Erro','Usuário Inválido!')
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
    port = 7008
    addr = ((ip, port))
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(addr)
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
