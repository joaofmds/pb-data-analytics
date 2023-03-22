"""
1. Apresente o ator/atriz com maior número de filmes e a respectiva quantidade.
"""

def ator_com_mais_filmes(arquivo_entrada):

    with open(arquivo_entrada, 'r') as arquivo:
        linhas = arquivo.readlines()
        cabecalho = linhas[0].strip().split(',')
        dados = []

        for linha in linhas[1::]:
            campos = linha.strip().split(',')
            
            if len(campos) == len(cabecalho) + 1:
                campos[0] += ', ' + campos.pop(0)
            
            dados.append(campos)
        
        indice_nome_autor = cabecalho.index('Actor')
        indice_numero_filmes = cabecalho.index('Number of Movies')

        ator_com_mais_filmes = None
        quantidade_filmes = 0

        for linha in dados:
            numero_filmes = float(linha[indice_numero_filmes])
            if numero_filmes > quantidade_filmes:
                quantidade_filmes = numero_filmes
                ator_com_mais_filmes = linha[indice_nome_autor]

    with open('etapa-1.txt', 'w') as arquivo:
        arquivo.write(f'Actor: {ator_com_mais_filmes} \nNumber of Movies: {quantidade_filmes}')

atores = ator_com_mais_filmes('actors.csv')