"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas Estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //execução do código
}

Python

for item in iteravel:
    //execução do código

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplo de iteráveis:
- String
    nome = 'Matheus Amorim'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

# Exemplo de for 1 (Iterando sobre uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

range(valor_inicial, valor_final)

OBS: O Valor final não é inclusive.

for numero in range(1, 10):
    print(numero)

Enumerate:

((0, 'M'), (1, 'a'), (2, 't'), (3, 'h'))

nome = 'Matheus Amorim'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  #Temos que transformar em uma lista

for indice, letra in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(v)

# Nao me preocupo com a variavél indice
for _, letra in enumerate(nome):
    print(v)   

for value in enumerate(nome):
    print(value)

# Somente os indicies
for value in enumerate(nome):
    print(value[0])

# Somente as letras 
for value in enumerate(nome):
    print(value[1])

qtd = int(input('Quantas vzs esse loop deve rodar? '))
soma = 0

#for n in range(qtd):
#   print(f'Imprimindo {n}')

for n in range(qtd):
    num = int(input(f'Informe o {n+1}/{qtd} valor: '))
    soma += num
print(f'A soma é {soma}')

nome = 'Nickolas Rocha'

# Não pular Linha ou modificar o final
for letra in nome:
    print(letra, end='')

"""

nome = 'Matheus '
nomeplus = nome + ' Amorim'

print(nomeplus)

nomemulti = nome * 30

print(nomemulti)

for num in range(10):
    print(f'{nome * num}')

