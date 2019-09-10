import datetime
from Pessoa import Pessoa

class buildP(object):
    def __init__(self):
        self._nome=None
        self._end=None
        self._cpf=None
        self._sexo=None
        self._nasc=None

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
    
    def Constroi(self):
        if self._nome == None:
            raise ValueError()
        if self._end == None:
            raise ValueError()
        if self._cpf == None:
            raise ValueError()
        if self._sexo == None:
            raise ValueError()
        if self._nasc == None:
            raise ValueError()
        return Pessoa(
            nome=self._nome,
            end=self._end,
            cpf=self._cpf,
            sexo=self._sexo,
            dataNasc=self._nasc
        )