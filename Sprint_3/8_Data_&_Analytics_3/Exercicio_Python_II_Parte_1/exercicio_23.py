"""
Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. 
Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração 
dos dois (resultados negativos são permitidos).

Utilize os valores abaixo para testar seu exercício:

x = 4 
y = 5
imprima:

Somando: 4+5 = 9
Subtraindo: 4-5 = -1
"""

class Calculo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def soma(self):
        return self.x + self.y
    
    def subtracao(self):
        return self.x - self.y
    

exercicios = Calculo(5, 4)
print(f'Somando {exercicios.x} + {exercicios.y} = {exercicios.soma()}')
print(f'Subtraindo {exercicios.x} - {exercicios.y} = {exercicios.subtracao()}')