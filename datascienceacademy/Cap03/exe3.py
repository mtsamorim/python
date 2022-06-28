# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista

numbers = (1, 2, 3, 4)
list1 = []

for i in numbers:
    aux = i * 2
    list1.append(aux)
    
print(list1)