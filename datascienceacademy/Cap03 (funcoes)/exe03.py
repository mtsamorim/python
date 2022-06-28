# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista
def listadd(arg):
    fruit1 = input("Qual a 1° fruta você vai adicionar?")
    fruit1 = fruit1.capitalize()
    fruit2 = input("Qual a 2° fruta você vai adicionar?")
    fruit2 = fruit2.capitalize()
    return arg.extend([fruit1, fruit2])

list1 = ['Maçã', 'Abacate', 'Abacaxi', 'Tangerina']

listadd(list1)

print(list1)