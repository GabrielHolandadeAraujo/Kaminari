from BuilderPessoa import buildP
from Pessoa import Pessoa
import datetime
import getpass
import socket, threading, pickle
from Pacotes import Pacote
import mysql.connector as mysql



class Thread(threading.Thread):
    def __init__(self,CSocket,Adress):
        threading.Thread.__init__(self)
        self.Sock=CSocket
        self.Ad=Adress
        print('Iniciada conexão com cliente',Adress)

    def run(self):
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
                    cursor.execute("select usuario,senha,tipodeUser from pessoa where usuario='{}'".format(mess[2]))
                    user=cursor.fetchall()
                    print(user)
                    print(user[0][2])
                    if len(user)==1 and user[0][2] == 1:
                        if user[0][1] == mess[3]:
                            retorno.append('True')
                        else:
                            retorno.append('False')
                            retorno.append('Pass')
                    else:
                        retorno.append('False')
                        retorno.append('User')
                elif mess[1] == 'FC':
                    cursor.execute("select usuario,senha,tipodeUser from pessoa where usuario='{}'".format(mess[2]))
                    user=cursor.fetchall()
                    print(user)
                    print(len(user))
                    if len(user)==1 and user[0][2] == 2:
                        if user[0][1] == mess[3]:
                            retorno.append('True')
                        else:
                            retorno.append('False')
                            retorno.append('Pass')
                    else:
                        retorno.append('False')
                        retorno.append('User')
                elif mess[1] == 'AD':
                    cursor.execute("select usuario,senha,tipodeUser from pessoa where usuario='{}'".format(mess[2]))
                    user=cursor.fetchall()
                    if len(user)==1 and user[0][2] == 3:
                        if user[0][1] == mess[3]:
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
                        cursor.execute("select * from pessoa where usuario='{}'".format(user))
                        cadastro = cursor.fetchall()
                        if len(cadastro)==0:
                            cursor.execute("select * from pessoa where CPF='{}'".format(cpf))
                            Cpef=cursor.fetchall()
                            if len(Cpef) == 0:
                                pessoa=(buildP().Nome(nome).CPF(cpf).Sexo(sexo).Email(email).End(end).Nascimento(nasc).User(user).Pass(pasw).Constroi())
                                print(pessoa)
                                if isinstance(pessoa,Pessoa):
                                    cursor.execute("insert into pessoa values('{}','{}','{}','{}','{}','{}','{}','{}',1)".format(pessoa.Cpf,pessoa.Nome,pessoa.End,pessoa.Sexo,pessoa.Nasc.strftime("%Y/%m/%d"),pessoa._email,pessoa.User,pessoa.Pass))
                                    conexao.commit()
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
                        cursor.execute("select * from pessoa where usuario='{}'".format(user))
                        cadastro = cursor.fetchall()
                        if len(cadastro)==0:
                            cursor.execute("select * from pessoa where CPF='{}'".format(cpf))
                            Cpef=cursor.fetchall()
                            if len(Cpef) == 0:
                                pessoa=(buildP().Nome(nome).CPF(cpf).Sexo(sexo).Email(email).End(end).Nascimento(nasc).User(user).Pass(pasw).Constroi())
                                print(pessoa)
                                if isinstance(pessoa,Pessoa):
                                    cursor.execute("insert into pessoa values('{}','{}','{}','{}','{}','{}','{}','{}',2)".format(pessoa.Cpf,pessoa.Nome,pessoa.End,pessoa.Sexo,pessoa.Nasc.strftime("%Y/%m/%d"),pessoa._email,pessoa.User,pessoa.Pass))
                                    conexao.commit()
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
                        cursor.execute("select * from pessoa where usuario='{}'".format(user))
                        cadastro = cursor.fetchall()
                        if len(cadastro)==0:
                            cursor.execute("select * from pessoa where CPF='{}'".format(cpf))
                            Cpef=cursor.fetchall()
                            if len(Cpef) == 0:
                                pessoa=(buildP().Nome(nome).CPF(cpf).Sexo(sexo).Email(email).End(end).Nascimento(nasc).User(user).Pass(pasw).Constroi())
                                print(pessoa)
                                if isinstance(pessoa,Pessoa):
                                    cursor.execute("insert into pessoa values('{}','{}','{}','{}','{}','{}','{}','{}',3)".format(pessoa.Cpf,pessoa.Nome,pessoa.End,pessoa.Sexo,pessoa.Nasc.strftime("%Y/%m/%d"),pessoa._email,pessoa.User,pessoa.Pass))
                                    conexao.commit()
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
                    peso,altura,comprimento,profundidade,eh_frágil,eh_expressa,remetente,destinatario,postadoem,vaipara = float(mess[2]),float(mess[3]),float(mess[4]),float(mess[5]),mess[6],mess[7],mess[8],mess[9],mess[10],mess[11]
                    if eh_frágil == 'Sim':
                        eh_frágil=1
                    else:
                        eh_frágil=0
                    if eh_expressa == 'Expresso':
                        eh_expressa=1
                    else:
                        eh_expressa=0
                    pac=Pacote(peso,altura,profundidade,comprimento,remetente,destinatario,postadoem,vaipara,eh_expressa,eh_frágil)
                    if not(isinstance(pac,Pacote)):
                        retorno.append('False')
                        retorno.append('Desc')
                    else:
                        cursor.execute("insert into pacotes values(DEFAULT,{},{},{},{},'{}','{}',{},{},{},'{}','{}')".format(pac.peso,pac.altura,pac.comprimento,pac.profundidade,pac.origem,pac.destino,pac.fragil,pac.tipo,pac.preco,pac.remetente,pac.destinatario))
                        conexao.commit()
                        cursor.execute('SELECT codigo FROM pacotes ORDER BY codigo DESC LIMIT 1')
                        ultimo=cursor.fetchall()
                        atualizacao = "O objeto foi postado em {} {}.".format(mess[10], datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
                        cursor.execute("INSERT INTO historico VALUES (DEFAULT, '{}', '{}')".format(ultimo[0][0], atualizacao))
                        conexao.commit()
                        print(ultimo)
                        retorno.append('True')
                        retorno.append('{}'.format(ultimo[0][0]))
                        retorno.append('{}'.format(pac.preco))
                else:
                    retorno.append('False')
                    retorno.append('Desc')
            elif(mess[0] == 'Email'):
                email = mess[1]
            elif(mess[0] == 'PAC'):
                #Teste pacote [PAC, CAL, Peso, Altura, Comprimento, Profundidade, Fragil, Tipo]
                #Atualiza PAC [PAC, ATT, codigo, chegou, saiu]
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
                elif(len(mess)==5):
                    #obj=procuraPacote(mess[2],pacotes)
                    cursor.execute("SELECT * FROM pacotes WHERE codigo = '{}' ".format(mess[2]))
                    lista = cursor.fetchall()
                    if(len(lista) == 1):
                        ob2 = Pacote(lista[0][1], lista[0][2], lista[0][4], lista[0][3], lista[0][10], lista[0][11], lista[0][5], lista[0][6], lista[0][8], lista[0][7])
                        ob2._codigo = lista[0][0]
                        #obj.atualizaHistorico(mess[3],mess[4])
                        atualizacao = "O objeto chegou em {} e partiu para {} {}.".format(mess[3], mess[4], datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
                        cursor.execute("INSERT INTO historico VALUES (DEFAULT, '{}', '{}')".format(lista[0][0], atualizacao))
                        conexao.commit()
                        cursor.execute("SELECT atualizacao FROM historico WHERE codigo = '{}' ".format(ob2.codigo))
                        ob2._historico = cursor.fetchall()
                        l2=[]
                        for i in ob2._historico:
                            l2.append(i[0])
                        ob2._historico=l2
                        retorno=ob2
                    else:
                        retorno.append('False')
                else:
                    retorno.append('False')
                    retorno.append('Desc')
            elif(mess[0] == 'RAS'):
                #[RAS,codigo]
                #obj=procuraPacote(mess[1],pacotes)
                cursor.execute("SELECT * FROM pacotes WHERE codigo = '{}' ".format(mess[1]))
                lista = cursor.fetchall()
                if(len(lista) == 1):
                    ob2 = Pacote(lista[0][1], lista[0][2], lista[0][4], lista[0][3], lista[0][10], lista[0][11], lista[0][5], lista[0][6], lista[0][8], lista[0][7])
                    ob2._codigo = lista[0][0]
                    cursor.execute("SELECT atualizacao FROM historico WHERE codigo = '{}' ".format(ob2.codigo))
                    ob2._historico = cursor.fetchall()
                    print('{}'.format(ob2.historico))
                    l2=[]
                    for i in ob2._historico:
                        l2.append(i[0])
                    ob2._historico=l2
                    retorno=ob2
                else:
                    retorno.append('False')
            elif(mess[0] == 'BUS'):
                #[BUS] retornar todos os funcionarios e adms
                #[BUS,cpf,2 || 3] retornar dados do funcionario/adm
                if(len(mess)==1):
                    cursor.execute("select nome,cpf,endereco from pessoa where tipoDeUser = 2")
                    func=cursor.fetchall()
                    cursor.execute("select nome,cpf,endereco from pessoa where tipoDeUser = 3")
                    adms=cursor.fetchall()
                    ret=[]
                    ret2=[]
                    aux=[]
                    for i in func:
                        aux.clear()
                        for x in range(len(i)):
                            aux.append(i[x])
                        ret.append(aux.copy())
                    for i in adms:
                        aux.clear()
                        for x in range(len(i)):
                            aux.append(i[x])
                        ret2.append(aux.copy())
                    retorno.append(ret.copy())
                    retorno.append(ret2.copy())
                elif(len(mess)==3):
                    cpf=mess[1]
                    tipo=mess[2]
                    cursor.execute('select nome,CPF,endereco,sexo,nascimento,email,tipoDeUser from pessoa where cpf="{}"'.format(cpf))
                    user=cursor.fetchall()
                    if(len(user)>0 and user[0][6]==int(tipo)):
                        for x in range(len(user[0])):
                            if isinstance(user[0][x],datetime.date):
                                data=user[0][x]
                                string=data.strftime("%d/%m/%Y")
                                retorno.append(string)
                            else:
                                retorno.append(user[0][x])
                        print(retorno)
                    else:
                        retorno.append('False')
                else:
                    retorno.append('False')
                    retorno.append('Desc')
            elif(mess[0] == 'DEL'):
                #[DEL,cpf]
                cpf=mess[1]
                sql="delete from pessoa where CPF = {};".format(cpf)
                cursor.execute(sql)
                conexao.commit()
                retorno.append('True')
            if isinstance(retorno,Pacote) or type(retorno[0]) == list:
                env = pickle.dumps(retorno)
                self.Sock.send(env)
            else:
                if len(retorno)==2:
                    env = '{},{}'.format(retorno[0],retorno[1])
                else:
                    if len(retorno)==1 and not('True' in retorno or 'False' in retorno):
                        env = '{},{}'.format(retorno[0][0],retorno[0][1])
                    elif len(retorno)==3:
                        env = '{},{},{}'.format(retorno[0],retorno[1],retorno[2])
                    else:
                        env = '{}'.format(retorno)
                        env=env.replace('[','')
                        env=env.replace(']','')
                        print(env)
                self.Sock.send(env.encode())
        print('Conexão Encerrada com Cliente',self.Ad)


op=1
users=[]
funcs=[]
admins=[]
pacotes=[]
admins.append(Pessoa('admin',None,None,None,None,None,'admin','admin'))
funcs.append(Pessoa('admin',None,None,None,None,None,'admin','admin'))
conexao = mysql.connect(host = 'localhost', user='root', passwd='root123456')
cursor = conexao.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS Kaminari')
cursor.execute('USE Kaminari')
cursor.execute("""CREATE TABLE IF NOT EXISTS pacotes
                (
                `codigo`       bigint NOT NULL AUTO_INCREMENT ,
                `peso`         double NOT NULL ,
                `altura`       double NOT NULL ,
                `comprimento`  double NOT NULL ,
                `profundidade` double NOT NULL ,
                `origem`       varchar(100) NOT NULL ,
                `destino`      varchar(100) NOT NULL ,
                `fragil`       tinyint NOT NULL ,
                `expresso`     tinyint NOT NULL ,
                `preco`        double NOT NULL ,
                `remetente`    varchar(100) NOT NULL ,
                `destinatario` varchar(100) NOT NULL ,

                PRIMARY KEY (`codigo`)
                )AUTO_INCREMENT = 1000000000000""")

cursor.execute("""CREATE TABLE IF NOT EXISTS `historico`
                (
                `codDeAtualizacao` bigint NOT NULL AUTO_INCREMENT,
                `codigo`      bigint NOT NULL ,
                `atualizacao` text NOT NULL ,
                PRIMARY KEY (`codDeAtualizacao`),
                FOREIGN KEY (`codigo`) REFERENCES `pacotes`(`codigo`)
                )ENGINE=InnoDB""")

cursor.execute("""CREATE TABLE IF NOT EXISTS `pessoa`
                (
                `CPF`        varchar(11) NOT NULL ,
                `nome`       varchar(100) NOT NULL ,
                `endereco`   text NOT NULL ,
                `sexo`       char NOT NULL ,
                `nascimento` date NOT NULL ,
                `email`      varchar(100) NOT NULL ,
                `usuario`    varchar(100) NOT NULL UNIQUE ,
                `senha`      varchar(100) NOT NULL ,
                `tipodeUser` int NOT NULL ,

                PRIMARY KEY (`CPF`)
                )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS `rastreia`
                (
                `idRastreio` bigint NOT NULL AUTO_INCREMENT ,
                `CPF`        varchar(11) NOT NULL ,
                `codigo`     bigint NOT NULL ,

                PRIMARY KEY (`idRastreio`),
                FOREIGN KEY (`CPF`) REFERENCES `pessoa` (`CPF`),
                FOREIGN KEY (`codigo`) REFERENCES `pacotes` (`codigo`)
                )""")

# cursor.execute('create table IF NOT EXISTS cod(PacStopped bigint DEFAULT 1000000000000)')
# cursor.execute('select * from pacotes')
# var=cursor.fetchall()
# if len(var)==0:
#     cursor.execute('insert into cod values(1000000000000)')
# else:


if __name__ == '__main__':
    LOCALHOST = ''
    PORT = 7001
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
