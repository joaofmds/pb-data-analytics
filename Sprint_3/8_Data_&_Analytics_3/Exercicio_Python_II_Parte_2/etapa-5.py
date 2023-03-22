"""
5. A lista dos atores ordenada pelo faturamento bruto total, em ordem decrescente.
"""

def autores_com_maior_faturamento_bruto(arquivo_entrada):
    with open(arquivo_entrada) as arquivo:
        linhas = arquivo.readlines()
        cabecalho = linhas[0].strip().split(',')
        dados = []

        for linha in linhas[1::]:
            campos = linha.strip().split(',')
            
            if len(campos) == len(cabecalho) + 1:
                campos[0] += ', ' + campos.pop(1)
            
            campos[1] = float(campos[1].strip())

            dados.append(campos)
        
        dados_ordenados = sorted(dados, key=retorna_faturamento_total, reverse=True)

    with open('etapa-5.txt', 'w') as arquivo:
        arquivo.write(f'Actors, Total Gross')
        for dado in dados_ordenados:
            arquivo.write(f'\n{dado[0]}, {dado[1]}')

def retorna_faturamento_total(campos):
    return campos[1]

teste = autores_com_maior_faturamento_bruto('actors.csv')