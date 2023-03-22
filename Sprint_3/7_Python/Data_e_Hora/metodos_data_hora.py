"""
Métodos de data e hora
"""

import datetime

# agora = datetime.datetime.now()
# print(agora)
# print(type(agora))
# print(repr(agora))

# hoje = datetime.datetime.today()
# print(hoje)
# print(repr(hoje))
# print(type(hoje))

# manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
# print(manutencao)

# manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
# print(manutencao.weekday())

# aniversario = input('Qual sua data de nascimento?')
# aniversario = aniversario.split('/')
# aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

# if aniversario.weekday() == 0:
#     print('Você nasceu em uma segunda-feira.')
# elif aniversario.weekday() == 1:
#     print('Você nasceu em uma terça-feira.')
# elif aniversario.weekday() == 2:
#     print('Você nasceu em uma quarta-feira.')
# elif aniversario.weekday() == 3:
#     print('Você nasceu em uma quinta-feira.')
# elif aniversario.weekday() == 4:
#     print('Você nasceu em uma sexta-feira.')
# elif aniversario.weekday() == 5:
#     print('Você nasceu em um sábado.')
# elif aniversario.weekday() == 6:
#     print('Você nasceu em um domingo.')

hoje = datetime.datetime.today()
print(hoje)
hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)