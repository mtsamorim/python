# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
def square(x):
    return x*x

def cube(x):
    return x*x*x

lista = [0, 1, 2, 3, 4]

funcs = [square, cube]

for i in lista:
    valor = [x(i) for x in funcs]
    print(list(valor))