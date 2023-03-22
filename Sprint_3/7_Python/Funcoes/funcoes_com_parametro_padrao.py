"""
Funções com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')

print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado())

def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3))
print(exponencial(3, 5))

# Obs: 
# Se o usuário passar osmente 1 argumento, este será atribuido ao parÂmetro número e será calculado o 
# quadrado desde número;
# Se o usuário passar 2 argumentos, o primeiro será atribuido ao parâmetro número e o segundo ao parâmetro
# potência. Então será calculada esta potência

print(exponencial())

# Obs: em funções Python, os parâmetros com valores default devem estar ao final da declaração

# Erro
def teste potencia, num=2):
    return num ** potencia

print(teste(6))

# Outros exemplos

def soma(num1=5, num2=2):
    return num1 + num2

print(soma(4, 3))
print(soma(4))
print(soma())

# Quais tipos de dados podemos utilizar como valores default para parâmetros?
# - Qualquer tipo de dado

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 3, subtracao))

instrutor = 'Geek'

def diz_oi():
    instrutor = 'Python'
    return f'Oi, {instrutor}'

print(diz_oi())

def diz_oi():
    prof = 'Geek'
    return f'Olá, {prof}'

print(diz_oi())

print(prof)

total = 0

def incrementa():
    global total 
    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
"""

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())