"""
Conhecendo o Pickle
"""

import pickle

class Animal:
    def __init__(self, nome):
        self.__nome = nome
    
    def comer(self):
        print(f'{self.__nome} está comendo')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self._Animal__nome} está miando')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self._Animal__nome} está latindo')

# felix = Gato('Félix')
# pluto = Cachorro('Pluto')

# with open('animais.pickle', 'wb') as arquivo:
#     pickle.dump({felix, pluto}, arquivo)

with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato._Animal__nome}')
    gato.mia()

    print(f'O cachorro chama-se {cachorro._Animal__nome}')
    cachorro.late()