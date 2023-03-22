"""
Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. 
Depois imprima a soma dos valores.

A string deve ter valor  "1,3,4,6,10,76"
"""

def soma_strings_de_numeros(string):
    lista_str = string.split(',')
    lista_int = []
    for i in lista_str:
        lista_int.append(int(i))
    return sum(lista_int)
    
string_para_somar = soma_strings_de_numeros("1,3,4,6,10,76")

print(string_para_somar)