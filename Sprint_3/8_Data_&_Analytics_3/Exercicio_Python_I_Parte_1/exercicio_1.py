"""
Exercícios Parte 1
Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa. 
Como saída, imprima o ano em que a pessoa completará 100 anos de idade.
"""

import datetime

def ano_que_completa_cem_anos(nome, idade):
    
    idade_int = int(idade)
    ano_atual = datetime.datetime.now().year
    ano_cem_anos = ano_atual - idade_int + 100
    return ano_cem_anos   

print(ano_que_completa_cem_anos('Felipe', 37))