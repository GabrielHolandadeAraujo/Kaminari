from BuilderPessoa import buildP
from Pessoa import Pessoa
import datetime
import getpass
import socket
from Pacotes import Pacote

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



host = ''
port = 7009
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reiniciliza o socket
serv_socket.bind(addr) #define a porta e quais ips podem se conectar com o servidor
serv_socket.listen(10) #define o limite de conexoes
print ('aguardando conexao')
con, cliente = serv_socket.accept()  # servidor aguardando conexao
print('conectado')
print('aguardando mensagem')
sai='0'

op=1
users=[]
funcs=[]
admins=[]
mess=''
while('exit' not in mess):
    retorno=[]
    recebe = con.recv(1024) #define que os pacotes recebidos sao de ate 1024 bytes
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
        else:
            retorno.append('False')
            retorno.append('Desc')
    elif(mess[0] == 'Email'):
        email = mess[1]
    elif(mess[0] == 'PAC'):
        #Teste pacote [PAC, CAL, Peso, Altura, Comprimento, Profundidade, Fragil, Tipo]
        if(len(mess) == 8):
            peso, alt, comp, prof, frag, tipo = mess[2], mess[3], mess[4], mess[5], mess[6], mess[7]
            if(mess[1] == 'CAL'):
                pak = Pacote(peso, alt, prof, comp, None, None, None, None, tipo, frag)
                retorno.append(str(pak.preco)       
        else:
            retorno.append('False')
            retorno.append('Desc')


    try:
        env = '{},{}'.format(retorno[0],retorno[1])
    except:
        try:
            env = '{},{}'.format(retorno[0][0],retorno[0][1])
        except:
            env=str(retorno)
    
    con.send(env.encode())

serv_socket.close()


'''while op!=0:
    op=int(input('1-Registrar\n0-sair\n\>'))
    if op == 1:
        try:
            nome=input('Digite seu nome: ')
            end=input('Endereço: ')
            cpf=input('Digite seu Cpf(apenas números): ')
            sexo=input('Sexo(M ou F): ')
            print('-Nascimento-')
            d=datetime.datetime(int(input('Ano:')),int(input('Mês:')),int(input('Dia:')))
            p=(buildP().Nome(nome).End(end).CPF(cpf).Sexo(sexo).Nascimento(d).Constroi())
            p._user=input('Digite um nome de usuário: ')
            p._pass=getpass.getpass('Digite uma senha: ')
            users.append(p)
        except:
            print('Insira valores validos em todos os campos!')
    elif op == 2:
        for x in users:
            print(x.Nome)
            print(x.End)
            print(x.Cpf)
            print(x.Sexo)
            print(x.Idade)
            print(x.usuario)
            print(x.password)
            print('--------------------')
'''