"""
Herança
"""

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

        def nome_completo(self):
            return f'{self.__nome} {self.__sobrenome}'
    
class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

        def nome_completo(self):
            return f'{self.__matricula} {self._Pessoa__nome}'
    
cliente1 = Cliente('Angelina', 'Julie', '123.456.789-10', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '109.876.543-21', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())