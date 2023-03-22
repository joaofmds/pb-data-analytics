"""
Documentando funções com Docstrings

OBS: Podemos ter acesso a documentação de uma função em Python
utilizando a propriedade especial __doc__

Podemos ainda fazer acesso a documentação com a função help()
"""

# Exemplos

print(help(print))

def diz_oi():
    """Uma função simples que retorna a string 'Oi'"""
    return 'Oi'

def exponencial(numero, potencia=2):
    """
    :param numero:
    :param potencia:
    :return:
    """
    return numero ** potencia
