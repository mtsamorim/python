# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista

list1 = []
var = 4 

while var <= 20:
    if var%2 == 0:
        list1.append(var)
    var += 1
    
print(list1)