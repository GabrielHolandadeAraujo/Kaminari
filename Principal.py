from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem
from Telas.Administrador import Ui_TelaAdmin
from Telas.CadastroUsuario import Ui_CadastroUsuario
from Telas.Esqueci import Ui_EsqueciaSenha
from Telas.Funcionario import Ui_Tela_Funcionario
from Telas.Login import Ui_Login
from Telas.Usuario import Ui_Usuario
from Pacotes import Pacote
import PyQt5
import sys
import os
import pickle
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
        self.tela_cadastro.cadUsuario.clicked.connect(self.cadastrar)

        self.tela_recup.voltar.clicked.connect(self.voltaLog)
        self.tela_recup.pushButton.clicked.connect(self.enviaEmail)

        self.tela_usuario.calculaFrete.clicked.connect(self.calculaPreco)
        self.tela_usuario.pushButton_2.clicked.connect(self.voltaLog)
        self.tela_usuario.Prastreia.clicked.connect(self.buscaPacote)
        self.tela_usuario.remPacote.clicked.connect(self.cancelaRastreio)
        self.tela_usuario.addPacote.clicked.connect(self.adicionaPacote)
        self.tela_usuario.pushButton.clicked.connect(self.atualizaPacotes)

        self.tela_func.pushButton_3.clicked.connect(self.voltaLog)

        self.tela_admin.pushButton_6.clicked.connect(self.voltaLog)
        self.tela_admin.pushButton.clicked.connect(self.CadastrarADM)
        self.tela_admin.pushButton_2.clicked.connect(self.todos)
        self.tela_admin.pushButton_3.clicked.connect(self.buscaPorCPF)
        self.tela_admin.pushButton_4.clicked.connect(self.buscaPorCPF)
        self.tela_admin.pushButton_5.clicked.connect(self.demitir)

        self.tela_func.CadEnc.clicked.connect(self.calculaPreco)
        self.tela_func.pushButton_2.clicked.connect(self.buscaPacote)
        self.tela_func.pushButton_7.clicked.connect(self.atualizaPacote)

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


    
    def cancelaRastreio(self):
        #PAC, RMM, user, codPac
        if len(self.tela_usuario.lineEdit_3.text()) > 0:
            cod = self.tela_usuario.lineEdit_3.text()
            name = self.tela_login.lineEdit.text()
            envia = 'PAC,RMM,{},{}'.format(name, cod)
            client_socket.send(envia.encode())
            recebe=client_socket.recv(4096)
            recebe=recebe.decode()
            if not('False' in recebe):
                self.tela_usuario.lineEdit_3.setText('')
                self.tela_usuario.prodRastreado.setText('')
                QtWidgets.QMessageBox.information(None, 'Confirmação', 'Pacote removido com sucesso.')
            else:
                QtWidgets.QMessageBox.information(None, 'Erro', 'Esse pacote não existe ou não está sendo rastreado por você.')
        else:
            QtWidgets.QMessageBox.information(None, 'Erro', 'Nenhum pacote foi rastreado.')

    def adicionaPacote(self):
        #PAC, RAS, user, codPac
        if len(self.tela_usuario.lineEdit_3.text()) > 0:
            cod = self.tela_usuario.lineEdit_3.text()
            name = self.tela_login.lineEdit.text()
            envia = 'PAC,RAS,{},{}'.format(name, cod)
            client_socket.send(envia.encode())
            recebe=client_socket.recv(4096)
            recebe=recebe.decode()
            if not('False' in recebe):
                self.tela_usuario.lineEdit_3.setText('')
                self.tela_usuario.prodRastreado.setText('')
                QtWidgets.QMessageBox.information(None, 'Confirmação', 'Pacote adicionado com sucesso.')
            else:
                QtWidgets.QMessageBox.information(None, 'Erro', 'Esse pacote não existe ou você já está rastreando ele.')
        else:
            QtWidgets.QMessageBox.information(None, 'Erro', 'Nenhum pacote foi rastreado.')
                    
    def atualizaPacotes(self):
        #PAC, ALL, user
        name = self.tela_login.lineEdit.text() 
        envia = 'PAC,ALL,{}'.format(name)
        client_socket.send(envia.encode())
        recebe=client_socket.recv(4096)
        lis=pickle.loads(recebe)
        pacotes=lis
        self.tela_usuario.textBrowser.setText('Código | Preço | Origem | Destino')
        for x in pacotes:
            print(x)
            self.tela_usuario.textBrowser.append('{} | {} R$ | {} | {}'.format(x[0],x[1],x[2], x[3]))

    def todos(self):
        envia='BUS'
        client_socket.send(envia.encode())
        recebe=client_socket.recv(4096)
        lis=pickle.loads(recebe)
        func=lis[0]
        adm=lis[1]
        self.tela_admin.textBrowser.setText('nome | cpf | endereco')
        for x in func:
            print(x)
            self.tela_admin.textBrowser.append('{} | {} | {}'.format(x[0],x[1],x[2]))
        self.tela_admin.textBrowser_2.setText('nome | cpf | tendereco')
        for x in adm:
            self.tela_admin.textBrowser_2.append('{} | {} | {}'.format(x[0],x[1],x[2]))
    
    def buscaPorCPF(self):
        if self.tela_admin.tabWidget.currentIndex() == 1:
            cpf=self.tela_admin.lineEdit_7.text()
            if not(self.tela_admin.radioButton_5.isChecked) and not(self.tela_admin.radioButton_6.isChecked):
                QtWidgets.QMessageBox.information(None,'Erro','Selecione funcionario ou administrador')
            else:
                if self.tela_admin.radioButton_5.isChecked():
                    tipo=2
                elif self.tela_admin.radioButton_6.isChecked():
                    tipo=3
                envia=[]
                envia.append('BUS')
                envia.append(cpf)
                envia.append(tipo)
                envia = '{},{},{}'.format(envia[0],envia[1],envia[2])
                client_socket.send(envia.encode())
                recebe=client_socket.recv(4096)
                recebe=recebe.decode()
                print(recebe)
                if not('False' in recebe):
                    nome,cpf,end,sex,nasc,email,tipo=recebe.split(',')
                    self.tela_admin.textBrowser_3.setText('Funcionario encontrado\n\n')
                    self.tela_admin.textBrowser_3.append('{}\n{}\n{}\n{}\n{}\n{}'.format(nome,cpf,end,sex,nasc,email))
                else:
                    self.tela_admin.textBrowser_3.setText('Funcionario não encontrado')
        else:
            cpf=self.tela_admin.lineEdit_8.text()
            if not(self.tela_admin.radioButton_8.isChecked) and not(self.tela_admin.radioButton_7.isChecked):
                QtWidgets.QMessageBox.information(None,'Erro','Selecione funcionario ou administrador')
            else:
                if self.tela_admin.radioButton_8.isChecked():
                    tipo=2
                elif self.tela_admin.radioButton_7.isChecked():
                    tipo=3
                envia=[]
                envia.append('BUS')
                envia.append(cpf)
                envia.append(tipo)
                envia = '{},{},{}'.format(envia[0],envia[1],envia[2])
                client_socket.send(envia.encode())
                recebe=client_socket.recv(4096)
                recebe=recebe.decode()
                print(recebe)
                if not('False' in recebe):
                    nome,cpf,end,sex,nasc,email,tipo=recebe.split(',')
                    self.tela_admin.textBrowser_4.setText('Funcionario encontrado\n\n')
                    self.tela_admin.textBrowser_4.append('{}\n{}\n{}\n{}\n{}\n{}'.format(nome,cpf,end,sex,nasc,email))
                else:
                    self.tela_admin.textBrowser_4.setText('Funcionario não encontrado')


    def esqueci(self):
        self.QtStack.setCurrentIndex(5)

    def demitir(self):
        cpf=self.tela_admin.lineEdit_8.text()
        if not(self.tela_admin.radioButton_8.isChecked) and not(self.tela_admin.radioButton_7.isChecked):
                QtWidgets.QMessageBox.information(None,'Erro','Selecione funcionario ou administrador')
        else:
            if self.tela_admin.radioButton_8.isChecked():
                tipo=2
            elif self.tela_admin.radioButton_7.isChecked():
                tipo=3
            envia=[]
            envia.append('BUS')
            envia.append(cpf)
            envia.append(tipo)
            envia = '{},{},{}'.format(envia[0],envia[1],envia[2])
            client_socket.send(envia.encode())
            recebe=client_socket.recv(4096)
            recebe=recebe.decode()
            print(recebe)
            if not('False' in recebe):
                nome,cpf,end,sex,nasc,email,tipo=recebe.split(',')
                op=QtWidgets.QMessageBox.question(self,'AVISO','Remover {}'.format(nome),QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
                if op ==QtWidgets.QMessageBox.Yes:
                    envia='{},{}'.format('DEL',cpf)
                    client_socket.send(envia.encode())
                    recebe=client_socket.recv(1024)
                    recebe=recebe.decode()
                    if 'True' in recebe:
                        QtWidgets.QMessageBox.information(None,'SUCESSO','Demitido com sucesso  ')
                else:
                    pass
            else:
                self.tela_admin.textBrowser_4.setText('Funcionario não encontrado')


    def voltaLog(self):
        self.tela_usuario.lineEdit.setText(''), self.tela_usuario.lineEdit_2.setText(''), self.tela_usuario.lineEdit_3.setText(''), self.tela_usuario.lineEdit_4.setText(''), self.tela_usuario.lineEdit_6.setText(''), self.tela_usuario.textBrowser.setText(''), self.tela_usuario.valorFrete.setText(''), self.tela_usuario.prodRastreado.setText('')
        self.tela_admin.lineEdit.setText(''), self.tela_admin.lineEdit_2.setText(''), self.tela_admin.lineEdit_3.setText(''), self.tela_admin.lineEdit_4.setText(''), self.tela_admin.lineEdit_5.setText(''), self.tela_admin.lineEdit_6.setText(''), self.tela_admin.lineEdit_7.setText(''), self.tela_admin.lineEdit_8.setText(''), self.tela_admin.textBrowser.setText(''), self.tela_admin.textBrowser_2.setText(''), self.tela_admin.textBrowser_3.setText(''), self.tela_admin.textBrowser_4.setText('')
        self.tela_func.lineEdit.setText(''), self.tela_func.lineEdit_2.setText(''), self.tela_func.lineEdit_3.setText(''), self.tela_func.lineEdit_4.setText(''), self.tela_func.lineEdit_5.setText(''), self.tela_func.lineEdit_6.setText(''), self.tela_func.lineEdit_7.setText(''), self.tela_func.lineEdit_8.setText(''), self.tela_func.lineEdit_9.setText(''), self.tela_func.lineEdit_20.setText(''), self.tela_func.lineEdit_21.setText(''), self.tela_func.textBrowser.setText(''), self.tela_func.textBrowser_2.setText(''), self.tela_func.Info_pacote.setText('')
        self.QtStack.setCurrentIndex(0)

    def atualizaPacote(self):
        #PAC, ATT, codigo, chegou, saiu
        cod, chegou, saiu = self.tela_func.lineEdit_9.text(), self.tela_func.lineEdit_20.text(), self.tela_func.lineEdit_21.text()
        envia = 'PAC,ATT,{},{},{}'.format(cod, chegou, saiu)
        client_socket.send(envia.encode())
        recebe = client_socket.recv(4096)
        try:
            obj = pickle.loads(recebe)
        except:
            obj = recebe.decode()
        if(isinstance(obj, Pacote)):
            self.tela_func.Info_pacote.setText('')
            self.tela_func.Info_pacote.setText('Remetente: {} | Destinatário: {}\n Origem: {} | Destino: {}\n É expressa: {} | É frágil: {}\n Peso: {}kg\n Altura: {}cm | Comprimento: {}cm | Profundidade: {}cm\n Preço: {} R$ \nHistórico:'.format(obj.remetente, obj.destinatario, obj.origem, obj.destino, obj.tipo, obj.fragil, obj.peso, obj.altura, obj.comprimento, obj.profundidade, obj.preco))
            for i in obj.historico:
                self.tela_func.Info_pacote.append(i)
            QtWidgets.QMessageBox.information(None, 'Confirmação', 'Pacote Atualizado com Sucesso')
            self.tela_func.lineEdit_20.setText(''), self.tela_func.lineEdit_21.setText('')
        else:
            QtWidgets.QMessageBox.information(None, 'Erro', 'Esse código não está cadastrado!')
    
    def calculaPreco(self):
        envia = ''
        recebe = ''
        if len(self.tela_func.lineEdit_3.text()) > 0 and len(self.tela_func.lineEdit_8.text()) > 0 and len(self.tela_func.lineEdit_7.text()) > 0 and len(self.tela_func.lineEdit_5.text()) > 0:
            peso, alt, comp, prof = self.tela_func.lineEdit_6.text(), self.tela_func.lineEdit_4.text(), self.tela_func.lineEdit.text(), self.tela_func.lineEdit_2.text()
            user = 'func'
            if(self.tela_func.radioButton.isChecked()):
                frag = 'Não'
            elif(self.tela_func.radioButton_2.isChecked()):
                frag = 'Sim'
            else:
                QtWidgets.QMessageBox.information(None,'Erro','O pacote é fragil?')
            if(self.tela_func.radioButton_3.isChecked()):
                tipo = 'Normal'
            elif(self.tela_func.radioButton_4.isChecked()):
                tipo = 'Expresso'
            else:
                QtWidgets.QMessageBox.information(None,'Erro','Selecione o tipo de entrega!')
        else:
            peso, alt, comp, prof = self.tela_usuario.lineEdit_6.text(), self.tela_usuario.lineEdit_4.text(), self.tela_usuario.lineEdit.text(), self.tela_usuario.lineEdit_2.text()
            user = 'user'
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
            if(user == 'user'):
                self.tela_usuario.valorFrete.setText('{} R$'.format(valor[1]))
            elif(user == 'func'):
                op=QtWidgets.QMessageBox.question(self,'AVISO','Preço {} R$\nDeseja cadastrar esse pacote?'.format(valor[1]),QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
                if(op == QtWidgets.QMessageBox.Yes):
                    self.cadastrarPacote()
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
        nome, cpf, email, end, user, pas = self.tela_cadastro.lineEdit.text(), self.tela_cadastro.lineEdit_2.text(), self.tela_cadastro.lineEdit_4.text(), self.tela_cadastro.lineEdit_6.text(), self.tela_cadastro.lineEdit_7.text(), self.tela_cadastro.lineEdit_8.text()
        nasc = self.tela_cadastro.dateEdit.text()
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
            self.tela_cadastro.lineEdit.setText(''), self.tela_cadastro.lineEdit_2.setText(''), self.tela_cadastro.lineEdit_4.setText(''), self.tela_cadastro.lineEdit_6.setText(''), self.tela_cadastro.lineEdit_7.setText(''), self.tela_cadastro.lineEdit_8.setText('')
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


    def cadastrarPacote(self):
        #CAD, PAC, peso, altura, comp, prof, fragil, tipo, remetente, destinatario, postado, vai
        recebe = ''
        peso, altura, comp, prof, remetente, destinatario, postado, vai = self.tela_func.lineEdit_6.text(), self.tela_func.lineEdit_4.text(), self.tela_func.lineEdit.text(), self.tela_func.lineEdit_2.text(), self.tela_func.lineEdit_3.text(), self.tela_func.lineEdit_8.text(), self.tela_func.lineEdit_7.text(), self.tela_func.lineEdit_5.text()
        if self.tela_func.radioButton.isChecked():
            frag = 'Não'
        elif self.tela_func.radioButton_2.isChecked():
            frag = 'Sim'
        else:
            QtWidgets.QMessageBox.information(None,'Erro','O pacote é frágil?')
        if self.tela_func.radioButton_3.isChecked():
            tipo = 'Normal'
        elif self.tela_func.radioButton_4.isChecked():
            tipo = 'Expresso'
        else:
            QtWidgets.QMessageBox.information(None,'Erro','Selecione o tipo de entrega!')
        envia = 'CAD,PAC,{},{},{},{},{},{},{},{},{},{}'.format(peso, altura, comp, prof, frag, tipo, remetente, destinatario, postado, vai)
        client_socket.send(envia.encode())
        recebe = client_socket.recv(1024)
        if('T' in recebe.decode()):
            QtWidgets.QMessageBox.information(None,'Confirmação','Pacote cadastrado com sucesso!')
            valor = ''
            valor = recebe.decode()
            valor = valor.split(',')
            self.tela_func.textBrowser.setText('{}'.format(valor[1]))
            self.tela_func.textBrowser_2.setText('{} R$'.format(valor[2]))
            #self.tela_func.lineEdit_6.setText(''), self.tela_func.lineEdit_4.setText(''), self.tela_func.lineEdit.setText(''), self.tela_func.lineEdit_2.setText(''), self.tela_func.lineEdit_3.setText(''), self.tela_func.lineEdit_8.setText(''), self.tela_func.lineEdit_7.setText(''), self.tela_func.lineEdit_5.setText(''), self.tela_func.textBrowser.setText(''), self.tela_func.textBrowser_2.setText('')
        else:
            QtWidgets.QMessageBox.information(None,'Erro','Preencha todos os campos!')

    def CadastrarADM(self):
        recebe=''
        nome, cpf, email, end, user, pas = self.tela_admin.lineEdit.text(), self.tela_admin.lineEdit_2.text(), self.tela_admin.lineEdit_4.text(), self.tela_admin.lineEdit_3.text(), self.tela_admin.lineEdit_5.text(), self.tela_admin.lineEdit_6.text()
        nasc=self.tela_admin.dateEdit.text()
        if self.tela_admin.radioButton.isChecked():
            sexo='M'
        elif self.tela_admin.radioButton_2.isChecked():
            sexo='F'
        else:
            QtWidgets.QMessageBox.information(None,'Erro','Selecione o sexo!')
        
        if self.tela_admin.radioButton_3.isChecked():
            tipo='FC'
        elif self.tela_admin.radioButton_4.isChecked():
            tipo='AD'
        else:
            QtWidgets.QMessageBox.information(None,'Erro','Selecione o tipo de conta!')
        envia = 'CAD,{},{},{},{},{},{},{},{},{}'.format(tipo,nome, cpf, sexo, email, end, nasc, user, pas)
        client_socket.send(envia.encode())
        recebe = client_socket.recv(1024)
        if('T' in recebe.decode()):
            QtWidgets.QMessageBox.information(None,'Confirmação','Cadastrado realizado com sucesso!')
            self.tela_admin.lineEdit.setText(''), self.tela_admin.lineEdit_2.setText(''), self.tela_admin.lineEdit_4.setText(''), self.tela_admin.lineEdit_6.setText(''), self.tela_admin.lineEdit_5.setText(''), self.tela_admin.lineEdit_3.setText('')
            self.QtStack.setCurrentIndex(3)
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


    def buscaPacote(self):
        if len(self.tela_func.lineEdit_9.text()) > 0:
            cod = self.tela_func.lineEdit_9.text()
            user = 'func'
        elif len(self.tela_usuario.lineEdit_3.text()) > 0:
            cod = self.tela_usuario.lineEdit_3.text()
            user = 'us'
        else:
            QtWidgets.QMessageBox.information(None, 'Erro', 'Informe o código!')
        envia = 'RAS,{}'.format(cod)
        client_socket.send(envia.encode())
        recebe = client_socket.recv(4096)
        print(type(recebe))
        try:
            print('pickle')
            obj = pickle.loads(recebe)
        except:
            print('decode')
            obj = recebe.decode()
        if(isinstance(obj, Pacote)):
            if(user == 'us'):
                self.tela_usuario.prodRastreado.setText('Remetente: {} | Destinatário: {}\n Origem: {} | Destino: {}\n É expressa: {} | É frágil: {}\n Peso: {}kg\n Altura: {}cm | Comprimento: {}cm | Profundidade: {}cm\n Preço: {} R$ \nHistórico:'.format(obj.remetente, obj.destinatario, obj.origem, obj.destino, obj.tipo, obj.fragil, obj.peso, obj.altura, obj.comprimento, obj.profundidade, obj.preco))
                
                for i in obj.historico:
                    self.tela_usuario.prodRastreado.append(i)
            else:
                self.tela_func.Info_pacote.setText('Remetente: {} | Destinatário: {}\n Origem: {} | Destino: {}\n É expressa: {} | É frágil: {}\n Peso: {}kg\n Altura: {}cm | Comprimento: {}cm | Profundidade: {}cm\n Preço: {} R$ \nHistórico:'.format(obj.remetente, obj.destinatario, obj.origem, obj.destino, obj.tipo, obj.fragil, obj.peso, obj.altura, obj.comprimento, obj.profundidade, obj.preco))
                print(obj.historico)
                for i in obj.historico:
                    self.tela_func.Info_pacote.append(i)
        else:
            QtWidgets.QMessageBox.information(None, 'Erro', 'Esse código não está cadastrado!')
            


    def entrar(self):
        enviar = 'LGIN'
        recebe = ''
        if self.tela_login.radioButton.isChecked():
            enviar = enviar + ',US' + ',' + self.tela_login.lineEdit.text() +  ',' + self.tela_login.lineEdit_2.text()
            client_socket.send(enviar.encode())
            recebe = client_socket.recv(1024)
            if('T' in recebe.decode()):
                self.QtStack.setCurrentIndex(2)
                #self.tela_login.lineEdit.setText(''), self.tela_login.lineEdit_2.setText('')
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
                self.tela_login.lineEdit.setText(''), self.tela_login.lineEdit_2.setText('')
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
                self.tela_login.lineEdit.setText(''), self.tela_login.lineEdit_2.setText('')
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
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are You Sure to Quit?', QMessageBox.No | QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    ip = input('Digite o ip da conexão:')
    port = 7001
    addr = ((ip, port))
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(addr)
    app = QApplication(sys.argv)
    show_main = Main()
    app.exec_()
    sai='exit'
    client_socket.send(sai.encode())
    sys.exit()
