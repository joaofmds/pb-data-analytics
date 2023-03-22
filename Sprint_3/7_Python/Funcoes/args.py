"""
Entendendo o *args
"""

# def soma_todos_numeros(num1=1, num2=2, num3=3):
#     return num1 + num2 + num3

# print(soma_todos_numeros(4, 6, 9))

# print(soma_todos_numeros(4, 9))  # TypeError

# print(soma_todos_numeros(4, 6, 9, 5))  # TypeError


# def soma_todos_numeros(*args):
#     return sum(args)

# print(soma_todos_numeros(4, 6, 9))

# print(soma_todos_numeros(4, 9)) 

# print(soma_todos_numeros(4, 6, 9, 5))

def soma_todos_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(soma_todos_numeros(*numeros))

