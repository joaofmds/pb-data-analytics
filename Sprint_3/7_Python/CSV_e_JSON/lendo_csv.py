"""
Lendo arquivos CSV
"""

with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    print(type(dados))
    print(dados)