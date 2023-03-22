"""
Implemente duas classes Pato e Pardal que herdem de uma classe Passaro a habilidade de voar e emitir som, porém, 
tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console.

Imprima no console exatamente assim:

Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu
"""

class Passaro:
    def __init__(self, nome):
        self.nome = nome

    def voar(self):
        print(f'{self.nome} voando...')

    def emitir_som(self):
        print(f'{self.nome} está emitindo som...')

class Pato(Passaro):
    def __init__(self, nome):
        super().__init__(nome)

    def voar(self):
        print(f'{self.nome} voando...')

    def emitir_som(self):
        print(f'{self.nome} está emitindo som...')
        print('Quack Quack')

class Pardal(Passaro):
    def __init__(self, nome):
        super().__init__(nome)

    def voar(self):
        print(f'{self.nome} voando...')

    def emitir_som(self):
        print(f'{self.nome} está emitindo som...')
        print('Piu piu')

donald = Pato('Donald')
donald.voar()
donald.emitir_som()

gervasio = Pardal('Gervásio')
gervasio.voar()
gervasio.emitir_som()