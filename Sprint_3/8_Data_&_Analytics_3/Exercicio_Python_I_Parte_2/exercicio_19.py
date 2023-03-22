"""
Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:

Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!

import random 
# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500),50)

Use as variáveis abaixo para representar cada operação matemática

mediana
media
valor_minimo 
valor_maximo 
"""

import random
import statistics

random_list = random.sample(range(500), 50)

def calcula_mediana(lista):
    metade = len(lista) // 2
    lista.sort()
    if not len(lista) % 2:
        return (lista[metade - 1] + lista[metade]) / 2.0
    return lista[metade]

mediana = calcula_mediana(random_list)

def calcula_media(lista):
    soma_lista = sum(lista)
    media = soma_lista / len(lista)
    return media
    
media = calcula_media(random_list)

def retorna_valor_minimo(lista):
    lista.sort()
    return lista[0]

valor_minimo = retorna_valor_minimo(random_list)

def retorna_valor_maximo(lista):
    lista.sort()
    lista.reverse()
    return lista[0]

valor_maximo = retorna_valor_maximo(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')