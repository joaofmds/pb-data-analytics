"""
Dada a seguinte lista:

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Faça um programa que gere uma nova lista contendo apenas números ímpares.
"""

def retorna_lista_impar(lista):
    lista_impar = []

    for i in lista:
        if i % 2 != 0:
            lista_impar.append(i)

    return lista_impar

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nova_lista = retorna_lista_impar(a)

print(nova_lista)