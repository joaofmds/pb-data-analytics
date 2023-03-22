"""
Dado o dicionário a seguir:

speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.
"""

def cria_lista(dicionario):
    lista = []
    for chave, valor in dicionario.items():
        lista.append(valor)
    set_lista = set(lista)
    nova_lista = list(set_lista)
    return nova_lista

speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

formata_dicionario = cria_lista(speed)

print(formata_dicionario)