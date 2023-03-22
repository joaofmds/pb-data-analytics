"""
Escreva um código Python para imprimir os números pares de 0 até 20 (incluso).

Importante: Aplique a função range() em seu código.
"""

def retorna_apenas_numeros_pares(numero):
    for i in range(numero):
        if i % 2 == 0:
            print(i)

numero = retorna_apenas_numeros_pares(21)