# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
def p(x):
    listaux = []
    for i in x:
        listaux.append(i*i*i)
    return listaux

list1 = [3, 5, 8]

print(p(list1))