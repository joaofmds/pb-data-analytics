"""
Deltas de Data e Hora
"""

import datetime

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2019, 3, 3, 9)

tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)