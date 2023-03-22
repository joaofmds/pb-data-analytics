"""
Atributos
"""

class Lampada:
    def __init__(self, voltagem, cor):
        self._voltagem = voltagem
        self_cor = cor
        self_ligada = False

    # @property
    # def voltagem(self):
    #     return self.voltagem
    
    # @property
    # def cor(self):
    #     return self.cor
    
    # @property
    # def ligada(self):
    #     return self.ligada

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self._numero = numero
        self._limite = limite
        self._saldo = saldo

class Produto:
    def __init__(self, nome, descricao, valor):
        self._nome = nome
        self._descricao = descricao
        self._valor = valor

class Usuario:
    def __init__(self, nome, email, senha):
        self._nome = nome
        self._email = email
        self._senha = senha

class Acesso:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha
    
    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.__email)

# user = Acesso('user@gmail.com', '123456')

# print(user.__email)

# print(user._Acesso__senha)

# user.mostra_senha()
# user.mostra_email()

# user1 = Acesso('user1@gmail.com', '123456')
# user2 = Acesso('user2@gmail.com', '654321')

# user1.mostra_email()
# user2.mostra_email()

# p1 = Produto('PlayStation 4', 'Video Game', 2300)
# p1 = Produto('X Box S', 'Video Game', 4500)

class Produto:

    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

# p1 = Produto('PlayStation 4', 'Video Game', 2300)
# p2 = Produto('X Box S', 'Video Game', 4500)

# print(p1.valor)

# print(p1.id)

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

p2.peso = '5 kg'
print(p2.peso)

del p2.peso
print(p2.peso)