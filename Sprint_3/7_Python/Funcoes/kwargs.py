"""
Entendendo o kwargs
"""

# def cores_favoritas(**kwargs):
#     for pessoa, cor in kwargs.items():
#         print(f'A cor favorita de {pessoa.title()} é {cor}')

# cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# def cumprimento_especial(**kwargs):
#     if 'geek' in kwargs and kwargs['geek'] == 'Python':
#         return 'Você recebeu um cumprimento pythonico'
#     elif 'geek' in kwargs:
#         return f"{kwargs['geek']} Geek!"
#     return 'Não tenho certeza de quem você é...'

# print(cumprimento_especial())
# print(cumprimento_especial(geek='Python'))
# print(cumprimento_especial(geek='Oi'))
# print(cumprimento_especial(geek='especial'))

# def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
#     print(f'{nome} tem {idade} anos')
#     print(args)
#     if solteiro:
#         print('Solteiro')
#     else:
#         print('Casado')
#     print(kwargs)

# minha_funcao(8, 'Julia')
# minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
# minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
# minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

