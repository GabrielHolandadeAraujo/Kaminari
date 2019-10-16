from BuilderPessoa import buildP
from Pessoa import Pessoa
import datetime
import getpass
import socket, threading, pickle
from Pacotes import Pacote



class Thread(threading.Thread):
    def __init__(self,CSocket,Adress):
        threading.Thread.__init__(self)
        self.Sock=CSocket
        self.Ad=Adress
        print('Iniciada conexão com cliente',Adress)

    def run(self):
        def cadastrado(user,lista):
            for x in lista:
                if x.User == user:
                    return x
            return False

        def CPF(cpf,lista):
            for x in lista:
                if x.Cpf == cpf:
                    return x
            return False

        def procuraPacote(codigo,lista):
            print('procurando por',codigo)
            for x in lista:
                print(x.codigo)
                if x.codigo == codigo:
                    return x
            return False

        mess=''
        while('exit' not in mess):
            retorno=[]
            recebe = self.Sock.recv(1024) #define que os pacotes recebidos sao de ate 1024 bytes
            print ('mensagem recebida: '+ recebe.decode())
            mess=recebe.decode()
            mess=mess.split(',')
            #testes com a tela de login [LGIN,TIPO,USER,SENHA]
            if mess[0]=='LGIN':
                if len(mess)<4:
                    retorno.append('False')
                    retorno.append('Desc')
                elif mess[1]=='US':
                    user=cadastrado(mess[2],users)
                    if user != False:
                        if user._pass == mess[3]:
                            retorno.append('True')
                        else:
                            retorno.append('False')
                            retorno.append('Pass')
                    else:
                        retorno.append('False')
                        retorno.append('User')
                elif mess[1] == 'FC':
                    user=cadastrado(mess[2],funcs)
                    if user != False:
                        if user._pass == mess[3]:
                            retorno.append('True')
                        else:
                            retorno.append('False')
                            retorno.append('Pass')
                    else:
                        retorno.append('False')
                        retorno.append('User')
                elif mess[1] == 'AD':
                    user=cadastrado(mess[2],admins)
                    if user != False:
                        if user._pass == mess[3]:
                            retorno.append('True')
                        else:
                            retorno.append('False')
                            retorno.append('Pass')
                    else:
                        retorno.append('False')
                        retorno.append('User')
                else:
                    retorno.append('False')
                    retorno.append('type')    
            #testes de cadastro [CAD,Type,Nome,CPF,Sexo,Email,Endereço,Nasc,User,Senha]
            elif mess[0]=='CAD':
                if len(mess)==10:
                    nome,cpf,sexo,email,end,user,pasw = mess[2],mess[3],mess[4],mess[5],mess[6],mess[8],mess[9]
                    dia,mes,ano=mess[7].split('/')
                    nasc=datetime.datetime(int(ano),int(mes),int(dia))
                    if mess[1]=='US':
                        cadastro = cadastrado(user,users)
                        if cadastro == False:
                            Cpef=CPF(cpf,users)
                            if Cpef == False:
                                pessoa=(buildP().Nome(nome).CPF(cpf).Sexo(sexo).Email(email).End(end).Nascimento(nasc).User(user).Pass(pasw).Constroi())
                                print(pessoa)
                                if isinstance(pessoa,Pessoa):
                                    users.append(pessoa)
                                    retorno.append('True')
                                else:
                                    retorno.append(pessoa)
                            else:
                                retorno.append('False')
                                retorno.append('CPF')
                        else:
                            retorno.append('False')
                            retorno.append('User')
                    elif mess[1]=='FC':
                        cadastro = cadastrado(user,funcs)
                        if cadastro == False:
                            Cpef=CPF(cpf,funcs)
                            if Cpef == False:
                                pessoa=(buildP().Nome(nome).CPF(cpf).Sexo(sexo).Email(email).End(end).Nascimento(nasc).User(user).Pass(pasw).Constroi())
                                if isinstance(pessoa,Pessoa):
                                    funcs.append(pessoa)
                                    retorno.append('True')
                                else:
                                    retorno.append(pessoa)
                            else:
                                retorno.append('False')
                                retorno.append('CPF')
                        else:
                            retorno.append('False')
                            retorno.append('User')
                    elif mess[1]=='AD':
                        cadastro = cadastrado(user,admins)
                        if cadastro == False:
                            Cpef=CPF(cpf,admins)
                            if Cpef == False:
                                pessoa=(buildP().Nome(nome).CPF(cpf).Sexo(sexo).Email(email).End(end).Nascimento(nasc).User(user).Pass(pasw).Constroi())
                                if isinstance(pessoa,Pessoa):
                                    admins.append(pessoa)
                                    retorno.append('True')
                                else:
                                    retorno.append(pessoa)
                            else:
                                retorno.append('False')
                                retorno.append('CPF')
                        else:
                            retorno.append('False')
                            retorno.append('User')
                elif len(mess)==12:
                    #[CAD,PAC,peso,altura,comprimento,profundidade,eh frágil?,eh expressa?,remetente,destinatario,postadoem,vaipara]
                    peso,altura,comprimento,profundidade,eh_frágil,eh_expressa,remetente,destinatario,postadoem,vaipara = int(mess[2]),int(mess[3]),int(mess[4]),int(mess[5]),mess[6],mess[7],mess[8],mess[9],mess[10],mess[11]
                    if eh_frágil == 'Sim':
                        eh_frágil=True
                    else:
                        eh_frágil=False
                    if eh_expressa == 'Expresso':
                        eh_expressa=True
                    else:
                        eh_expressa=False
                    pac=Pacote(peso,altura,profundidade,comprimento,remetente,destinatario,postadoem,vaipara,eh_expressa,eh_frágil)
                    if not(isinstance(pac,Pacote)):
                        retorno.append('False')
                        retorno.append('Desc')
                    else:
                        retorno.append('True')
                        retorno.append('{}'.format(pac.codigo))
                        retorno.append('{}'.format(pac.preco))
                        pacotes.append(pac)
                else:
                    retorno.append('False')
                    retorno.append('Desc')
            elif(mess[0] == 'Email'):
                email = mess[1]
            elif(mess[0] == 'PAC'):
                #Teste pacote [PAC, CAL, Peso, Altura, Comprimento, Profundidade, Fragil, Tipo]
                if(len(mess) == 8):
                    peso, alt, comp, prof, frag, tipo = float(mess[2]), float(mess[3]), float(mess[4]), float(mess[5]), mess[6], mess[7]
                    if(tipo == 'Normal'):
                        tipo = False
                    else:
                        tipo = True
                    if(mess[1] == 'CAL'):
                        pak = Pacote(peso, alt, prof, comp, None, None, None, None, tipo, frag)
                        retorno.append('T')
                        retorno.append(str(pak.preco))       
                else:
                    retorno.append('False')
                    retorno.append('Desc')
            elif(mess[0] == 'RAS'):
                #[RAS,codigo]
                obj=procuraPacote(mess[1],pacotes)
                if not(type(obj) == bool):
                    retorno=obj
                else:
                    retorno.append('False')
            if isinstance(retorno,Pacote):
                env = pickle.dumps(retorno)
                self.Sock.send(env)
            else:
                if len(retorno)==2:
                    env = '{},{}'.format(retorno[0],retorno[1])
                else:
                    if len(retorno)==1 and not('True' in retorno):
                        env = '{},{}'.format(retorno[0][0],retorno[0][1])
                    elif len(retorno)==3:
                        env = '{},{},{}'.format(retorno[0],retorno[1],retorno[2])
                    else:
                        env = '{}'.format(retorno)
                self.Sock.send(env.encode())
        print('Conexão Encerrada com Cliente',self.Ad)


op=1
users=[]
funcs=[]
admins=[]
pacotes=[]
admins.append(Pessoa('admin',None,None,None,None,None,'admin','admin'))
funcs.append(Pessoa('admin',None,None,None,None,None,'admin','admin'))

if __name__ == '__main__':
    LOCALHOST = ''
    PORT = 7008
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Servidor iniciado!")
    print("Aguardando nova conexao..")
    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = Thread(clientsock,clientAddress)
        newthread.start()
