import random
import numpy as np

x = random.random()
print(x)

random.seed(777)

x = []
for i in range(100):
    x.append(random.random())

len(x)

nomes = ['Lucas', 'Marcos', 'Thiago', 'Roberto', 'Bianca', 'Erika']

random.choice(nomes)

random.shuffle(nomes)

random.sample(nomes, 4)
