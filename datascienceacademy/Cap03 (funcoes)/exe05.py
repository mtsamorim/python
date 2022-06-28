# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles
soma = lambda x,y: x+y

num1 = int(input("Qual o 1° numero?"))
num2 = int(input("Qual o 2° numero?"))

print(soma(num1, num2))