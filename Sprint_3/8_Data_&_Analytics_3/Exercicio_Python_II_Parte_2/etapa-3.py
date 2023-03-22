"""
3. Apresente o ator/atriz com a maior média de faturamento por filme.
"""
def ator_maior_media_faturamento():
    
    with open('etapa-2.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        cabecalho = linhas[0].strip().split(',')
        dados = []

        for linha in linhas[1::]:
            campos = linha.strip().split(',')
            
            if len(campos) == len(cabecalho) + 1:
                campos[0] += ', ' + campos.pop(0)
            
            dados.append(campos)

        indice_nome_autor = cabecalho.index('Actor')
        indice_faturamento_medio = cabecalho.index('Average Biiling')

        ator_maior_faturamento = None
        faturamento_medio = 0

        for linha in dados:
            maior_faturamento = float(linha[indice_faturamento_medio])
            if maior_faturamento > faturamento_medio:
                faturamento_medio = maior_faturamento
                ator_maior_faturamento = linha[indice_nome_autor]

    with open('etapa-3.txt', 'w') as arquivo:
        arquivo.write(f'Actor: {ator_maior_faturamento} \nAverage Biiling: {faturamento_medio}')

maior_faturmanto_médio = ator_maior_media_faturamento()