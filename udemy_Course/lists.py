"""
Python:

 - Não possuem tamanho fixo como em C e Java
 - Não possuem dado fixo, pode ser adicionado qualquer tipo de dado 

 As listas em python são declaradas com colchetes: []

"""
'''

list2 = [1, 'batum', [1,2,3]]

#verifica o tipo do elemento
#print(type(list1))
#print(type(list2))

for i in range(len(list1)):
    print(type(i))
'''

"""
list1 = ['GeEk UniversityE']

#conta quantas letras E tem string dentro da lista
for i in list1:
    for x in i:
        count+=1

for i in range(len(list1)):
    for j in range(count):
        if list1[i][j] == 'e' or list1[i][j] == 'E':
            count2+=1

print(count2)
"""

"""
list1 = [22, 33 ,44 ,55 ,66 ,77 ,88 ,99]

#insere o elemento 1 na posição 1 que é a do 33 e ele é deslocado para a direita
list1.insert(1, 1)
print(list1)
"""

'''
list1 = [11,22,33,44,55,66,77,88]

#Tira o ultimo elemento
#list1.pop()
#print(list1)

#Tira o elemento 33 e todos os elementos à direita dele são deslocados para a esqueda
list1.pop(2)
print(list1)
'''

'''
list1 = [1, 2, 3]

#repetimos os elemntos da lista
list1 = list1 * 3

print(list1)
'''

'''
word = 'O Rato roeu a roupa do rei'

#transforma a string em uma lista usando o ' ' de referencia na hora da separação
aux = word.split()

print(aux)

word2 = 'O?Rato?roeu?a?roupa?do?rei'

#transforma a string em uma lista usando o '?' de referencia na hora da separação
aux2 = word2.split('?')

print(aux2)
'''

'''
list1 = ['O', 'Rato', 'roeu', 'a', 'roupa', 'do', 'rei']

#pega os elementos da lista e tranforma em uma string separando elas com o caractere que voce decidir, nesse caso foi o espaço
word = ' '.join(list1)

print(word)

print(type(word))
'''

'''
list1 = [12, 2, 456, 11, 400]

print(sum(list1)) #soma os elementos da lista
print((max(list1)) #pega o maior elemento
print(min(list1)) #pega o menor elemento
'''

'''
#Deep Copy
list1 = [1, 2, 3]

#copia a lista para uma outra lista, não modificando a lista principal
newlist1 = list1.copy()

newlist1.append(4)

print(list1)
print(newlist1)
'''

'''
#Shallow Copy
list1 = [1, 2, 3]

#copia a lista para uma outra lista, modificando a lista principal
newlist1 = list1

newlist1.append(4)

print(list1)
print(newlist1)
'''