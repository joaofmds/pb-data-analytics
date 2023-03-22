"""
Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento.
Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.

Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.
"""

def quadrado(numero):
    return numero ** 2

def my_map(lista, funcao):
    nova_lista = []
    for numero in lista:
        nova_lista.append(funcao(numero))
    return nova_lista


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nova_lista = my_map(my_list, quadrado)
print(nova_lista)