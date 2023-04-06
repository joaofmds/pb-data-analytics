import matplotlib.pyplot as plt
import seaborn as sns

y = [2, 5, 2, 7, 5, 1]
x = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6']
x2 = ['Variável Um', 'Variável Dois', 'Variável Três', 'Variável Quatro', 'Variável Cinco', 'Variável Seis']

# plt.barh(x2, y, color='g')
# plt.xlabel('Variável eixo X', size=24) 
# plt.ylabel('Categorias', size=20)
# plt.title('Título do meu gráfico')

# plt.bar(x2, y)

sns.barplot(x, y)
