import datetime
from Pacotes import Pacote
class Pessoa(object):
    __slots__ = ['_nome','_end','_cpf','_sexo','_nasc','_user','_pass', '_pacotes','_email']

    def __init__(self,nome,end,cpf,sexo,dataNasc,email):
        self._nome=nome
        self._end=end
        self._cpf=cpf
        self._sexo=sexo
        self._nasc=dataNasc
        self._email=email
        self._pacotes=[] 
        self._user=None
        self._pass=None 
    
    def adiconaPacote(self, pacote):
        if isinstance(pacote, Pacote):
            self._pacotes.append(pacote)
            return True
        else:
            return False 

    @property
    def usuario(self):
        return self._user

    @usuario.setter
    def usuario(self, user):
        if(len(user)<1):
            raise Exception('Preencha o usuario')
        else:
            self._user = user

    @property
    def password(self):
        return self._pass

    @password.setter
    def password(self, passe):
        if(len(passe)<1):
            raise Exception('Preencha a senha')
        else:
            self._pass = passe

    @property
    def Nome(self):
        return self._nome

    @Nome.setter
    def Nome(self,nome):
        if len(nome)<1:
            raise Exception('Preencha o nome')
        else:
            self._nome=nome

    @property
    def End(self):
        return self._end

    @End.setter
    def End(self,end):
        if len(end)<1:
            raise Exception('preencha o endereco')
        else:
            self._end=end

    @property
    def Cpf(self):
        return self._cpf

    @property
    def Sexo(self):
        return self._sexo

    @property
    def Nasc(self):
        return self._nasc

    @property
    def Idade(self):
        temp = (datetime.datetime.now() - self._nasc).days
        return temp//365

