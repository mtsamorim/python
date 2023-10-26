# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos
def numbers(*arg):
    for i in arg:
        print(i)

numbers(1, 2 , 3, 4)