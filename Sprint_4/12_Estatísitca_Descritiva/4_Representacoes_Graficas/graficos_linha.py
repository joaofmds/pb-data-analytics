import matplotlib.pyplot as plt

y = [6, 8, 3, 1, 9]
x1 = [1, 2, 3, 4, 5]
x = ['seg', 'ter', 'qua', 'qui', 'sex']

plt.plot(x1, y, '*-g')
plt.xlabel('Eixo X', size=20)
plt.ylabel('Eixo Y', size=20)
plt.title('Título do gráfico', size=15)
plt.show()