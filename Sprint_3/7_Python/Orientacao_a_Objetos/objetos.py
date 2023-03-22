"""
Objetos
"""

class Lampada:
    def __init__(self, voltagem, cor, luminosidade):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada
    
    def liga_desliga(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:
    
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz_oi(self):
        print(f'O cliente {self.__nome} diz oi')

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

# lamp1 = Lampada('branca', 110, 60)

# lamp1.liga_desliga()

# print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

# cc1 = ContaCorrente(5000, 20000)

# user1 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

cli1 = Cliente('Angeline Julie', '123.456.789-10')

cc = ContaCorrente(5000, 10000, cli1)

cc.mostra_cliente()

cc._ContaCorrente__cliente.diz_oi()