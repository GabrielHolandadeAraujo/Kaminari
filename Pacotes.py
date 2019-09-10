import datetime

class Pacote(object):
    _porcmqua = 0.01
    _porpeso = 0.20
    _contador = 0
    def __init__(self, peso, altura, profundidade, comprimento, origem, destino, tipo, fragil):
        self._peso = peso    
        self._altura = altura
        self._profundidade = profundidade
        self._comprimento = comprimento
        self._origem = origem
        self._destino = destino
        self._historico = []
        self._fragil = fragil
        self._expresso = tipo
        self._preco = 0
        self.atualizaPreco()
        self._codigo = str(datetime.datetime.now().year)+str(Pacote._contador).zfill(12)
        Pacote._contador += 1

    def atualizaHistorico(self, chegou, vai):
        self._chegou = chegou
        self._vai = vai
        self._historico.append("O objeto chegou em {} e partiu para {} {}.".format(self._chegou, self._vai, datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))

    def mostraHistorico(self):
        print('Histórico:')
        for i in self._historico:
            print(i)
        print()

    def atualizaPreco(self):
        if(self._expresso == True):
            self._preco = (self._altura * self._profundidade * self._comprimento * Pacote._porcmqua) + (self._peso * Pacote._porpeso) + 40.00
        else:
            self._preco = (self._altura * self._profundidade * self._comprimento * Pacote._porcmqua) + (self._peso * Pacote._porpeso) + 2

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, pe):
        if(pe > 0.0 and pe < 800.0):
            self._peso = pe
            self.atualizaPreco()
            True
        else:
            False

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, al):
        if(al > 0.0 and al < 500.0):
            self._altura = al
            self.atualizaPreco()
            True
        else:
            False

    @property
    def profundidade(self):
        return self._profundidade

    @profundidade.setter
    def profundidade(self, prof):
        if(prof > 0.0 and prof < 500.0):
            self._profundidade = prof
            self.atualizaPreco()
            True
        else:
            False

    @property
    def comprimento(self):
        return self._comprimento

    @comprimento.setter
    def comprimento(self, comp):
        if(comp > 0.0 and comp < 500.0):
            self._comprimento = comp
            self.atualizaPreco()
            True
        else:
            False

    @property
    def origem(self):
        return self._origem

    @property
    def destino(self):
        return self._destino

    @property
    def codigo(self):
        return self._codigo

    @property
    def tipo(self):
        return self._tipo

    @property
    def preco(self):
        return self._preco

    @property
    def historico(self):
        return self._historico


p1 = Pacote(4, 10, 12, 8, 'Curitiba', 'Picos', True, True)
p2 = Pacote(4, 30, 19, 5, 'Teresina', 'Floriano', False, False)
p1.atualizaHistorico('Chico Santo', 'Teresina')
p1.atualizaHistorico('Teresina', 'Picos')
p1.mostraHistorico()

print("Peso: {}\nDimensoes: {}x{}x{}\nOrigem: {}\nDestino {}\nPreco: {}\nCodigo: {}\n".format(p1.peso,p1.altura,p1.profundidade,p1.comprimento, p1.origem, p1.destino, p1.preco, p1.codigo))
print("Peso: {}\nDimensoes: {}x{}x{}\nOrigem: {}\nDestino {}\nPreco: {}\nCodigo: {}\n".format(p2.peso,p2.altura,p2.profundidade,p2.comprimento, p2.origem, p2.destino, p2.preco, p2.codigo))