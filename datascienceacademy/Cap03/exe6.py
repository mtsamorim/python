# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

count = 0

while count < 100:
    print(count)
    if count == 23:
        break
    count += 1