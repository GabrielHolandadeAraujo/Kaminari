import datetime
from Pessoa import Pessoa

class buildP(object):
    def __init__(self):
        self._nome=None
        self._end=None
        self._cpf=None
        self._sexo=None
        self._nasc=None
        self._email=None
        self._user=None
        self._pass=None

    def Nome(self,nome):
        if nome==type(str) or len(nome)<=80:
            self._nome=nome
        return self

    def End(self,end):
        if len(end)>0:
            self._end=end
        return self

    def CPF(self,cpf):
        if len(cpf)==11:
            self._cpf=cpf
        return self

    def Sexo(self,sexo):
        if sexo == 'M' or sexo == 'F':
            self._sexo=sexo
        return self

    def Nascimento(self,data):
        temp=datetime.datetime.now()-data
        if (isinstance(data,datetime.datetime)and(temp.days//365)>=18):
            self._nasc=data
        return self

    def User(self,user):
        if len(user) > 5:
            self._user=user
        return self

    def Pass(self,pswd):
        if len(pswd) > 5:
            self._pass=pswd
        return self

    def Email(self,email):
        if '@' in email and '.' in email:
            self._email=email
        return self
    
    def Constroi(self):
        Err=['Err']
        if self._nome == None:
            Err.append('Nome')
            return Err
        if self._end == None:
            Err.append('End')
            return Err
        if self._cpf == None:
            Err.append('CPF')
            return Err
        if self._sexo == None:
            Err.append('Sexo')
            return Err
        if self._nasc == None:
            Err.append('Nasc')
            return Err
        if self._user == None:
            Err.append('User')
            return Err
        if self._pass == None:
            Err.append('Pass')
            return Err
        if self._email == None:
            Err.append("Email")
            return Err
        return Pessoa(
            nome=self._nome,
            end=self._end,
            cpf=self._cpf,
            sexo=self._sexo,
            dataNasc=self._nasc,
            email=self._email,
            user=self._user,
            pswd=self._pass
        )