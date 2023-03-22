"""
2. Apresente a  média de faturamento bruto por ator.
"""
def media_faturamento_bruto(arquivo_entrada):

    with open(arquivo_entrada, 'r') as arquivo:
        linhas = arquivo.readlines()
        cabecalho = linhas[0].strip().split(',')
        dados = []

        for linha in linhas[1::]:
            campos = linha.strip().split(',')
            
            if len(campos) == len(cabecalho) + 1:
                campos[0] += ', ' + campos.pop(1)
        
            dados.append(campos)
        
        indice_nome_autor = cabecalho.index('Actor')
        indice_faturamento_bruto_total = cabecalho.index('Total Gross')
        indice_numero_filmes = cabecalho.index('Number of Movies')

        armazenamento_informacoes = {}

        for linha in dados:
            ator = linha[indice_nome_autor]
            faturamento_bruto = float(linha[indice_faturamento_bruto_total])
            quantidade_filmes = int(linha[indice_numero_filmes])
            faturamento_medio = faturamento_bruto / quantidade_filmes
            armazenamento_informacoes.update({ator: faturamento_medio})

    with open('etapa-2.txt', 'a') as arquivo:
        arquivo.write('Actor,Average Biiling')
        for ator, faturamento_medio in armazenamento_informacoes.items():
            arquivo.write(f'\n{ator}, {faturamento_medio}')

media_faturamento = media_faturamento_bruto('actors.csv')