"""
Métodos
"""

from passlib.hash import pbkdf2_sha256 as cryp

class Lampada:
    def __init__(self, voltagem, cor, luminosidade):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__luminosidade = luminosidade
        self._ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo

class Produto:

    contador = 0
    
    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor

    def desconto(self, porcentagem):
        return (self.__valor * (100 - porcentagem)) / 100

class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuários no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.encrypt(senha, round=200000, salt_size=10)
        Usuario.contador = self.id
        print(f'Usuário criado: {self.__gera_uduario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    
    def __gera_uduario(self):
        return self.__email.split('@')[0]
    


# p1 = Produto('PlayStation 4', 'Video Game', 2300)

# print(p1.desconto(10))

# user1 = Usuario('Angeline', 'Julie', 'angeline@gmail.com', '123456')
# user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

# print(user1.nome_completo())
# print(user2.nome_completo())

# nome = input('Informe o nome: ')
# sobrenome = input('Informe o sobrenome: ')
# email = input('Informe o email: ')
# senha = input('Informe a senha: ')
# confirma_senha = input('Confirme a senha: ')

# if senha == confirma_senha:
#     user = Usuario(nome, sobrenome, email, senha)
# else:
#     print('Senha não confere...')
#     exit(42)

# print('Usuário criado com sucesso!')

# senha = input('Informe a senha para acesso: ')

# if user.checa_senha(senha):
#     print('Acesso permitido')
# else:
#     print('Acesso negado')

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

