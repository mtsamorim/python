# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

fruits = ['Abacate', 'Abacaxi', 'Morango', 'Caju', 'Kiwi']
v = False

for i in fruits:
    if i == 'Morango':
        v = True
        
if v == True:
    print("Morango encontrado!")
else:
    print("Morango não encontrado!")