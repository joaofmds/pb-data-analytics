"""
4. O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
"""

def filme_mais_frequente(arquivo_entrada):
    with open(arquivo_entrada) as arquivo:
        linhas = arquivo.readlines()
        cabecalho = linhas[0].strip().split(',')
        dados = []

        filmes_frequencia = {}

        for linha in linhas[1::]:
            campos = linha.strip().split(',')
            
            if len(campos) == len(cabecalho) - 1:
                campos[0] += ', ' + campos.pop(0)
            
            filmes = campos[4].split(';')
            for filme in filmes:
                if filme not in filmes_frequencia:
                    filmes_frequencia[filme] = 1
                else:
                    filmes_frequencia[filme] += 1

        filmes_mais_frequentes = []
        frequencia_maxima = 0
        for filme, frequencia in filmes_frequencia.items():
            if frequencia > frequencia_maxima:
                filmes_mais_frequentes = [filme]
                frequencia_maxima = frequencia
            elif frequencia == frequencia_maxima:
                filmes_mais_frequentes.append(filme)

        with open('etapa-4.txt', 'w') as arquivo:
            arquivo.write(f'#1 Movie: {filmes_mais_frequentes} \nFrequency: {frequencia_maxima}')

filme = filme_mais_frequente('actors.csv')