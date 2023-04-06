import matplotlib.pyplot as plt
import seaborn as sns

y = [2, 5, 2, 7, 5, 1]
x = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6']
x2 = ['Variável Um', 'Variável Dois', 'Variável Três', 'Variável Quatro', 'Variável Cinco', 'Variável Seis']

plt.pie(y, labels=x, radius=2)
plt.show()