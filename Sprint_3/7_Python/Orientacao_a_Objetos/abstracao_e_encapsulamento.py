"""
Abstração e Encapsulamento
"""

class Conta:

    contador = 400

    def __init__(self, titular, limite, saldo):
        self.__numero = Conta.contador 
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

conta1 = Conta('Geek', 150.00, 1500)

print(conta1.numero)