"""
Tuple 

1 - Tuples são representas por ()

2 - As tuples são imutaveis 

tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(type(tuple1))

tuple2 = 1, 2, 3, 4, 5
print(tuple2)
print(type(tuple2))

#OBS: Cuidado com tuple de um item [Tuples são definidas pela , e não pelos ()]

tuple3 = (1) #Isso não é uma tuple
print(tuple3)
print(type(tuple3))

tuple4 = (1,) #Isso é uma tuple
print(tuple4)
print(type(tuple4))

#Desempacotamente de tuple

tuple1 = ('Carro', 'Ronaldo')

vel, nome  = tuple1

print(type(tuple1))

print(vel)

print(nome)

#Concatenação de tuple

tuple1 = (1, 2, 3)
print(tuple1)

tuple2 = (4, 5, 6)
print(tuple2)

print(tuple1 + tuple2)

print(tuple1)
print(tuple2)

tuple1 = tuple1 + tuple2 #São imutaveis mas podemos sobrescrever seus valores
print(tuple1)

#Contando elementos dentro de uma tuple

tuple1 = ('a', 'b', 'c', 'd', 'e')

print(tuple1.count('c'))

escola = tuple('Mamadeira')
print(escola)

print(escola.count('a'))

Pq utilizar tuples?

- Mais eficientes que lista
- Tuple deixa o códgio mais seguro

"""

#Copy tuple

tuple1 = (1, 2, 3, 4)

nova = tuple1

print(nova)
print(type(nova))
print(tuple1)