from BuilderPessoa import buildP
import datetime
import getpass

op=1
users=[]
while op!=0:
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
