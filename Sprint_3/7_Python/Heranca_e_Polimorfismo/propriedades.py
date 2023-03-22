"""
Propriedades
"""

class Conta:
    
    contador = 0
    
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor):
        self.__valor += valor    

    def sacar(self, valor):
        self.__valor -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    # def get_numero(self):
    #     return self.__numero
    
    # def get_titular(self):
    #     return self.__titular
    
    # def set_titular(self, titular):
    #     self.__titular = titular
    
    # def get_saldo(self):
    #     return self.__saldo
    
    # def get_limite(self):
    #     return self.__limite

    # def get_limite(self, limite):
    #     self.__limite = limite