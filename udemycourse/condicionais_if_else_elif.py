"""
Estruturas Condicionais if, else e elif
"""

idade = int(input())

# Certo
if idade < 18:
    print('Menor de Idade')
elif idade == 18:
    print('Tem 18 Anos')
elif idade == 27:
    print('Tem 27 Anos')
else:
    print('Maior de Idade')


# Errado
if idade < 18:
    print('Menor de Idade')

elif idade == 18:
    print('Tem 18 Anos')

elif idade == 27:
    print('Tem 27 Anos')

else:
    print('Maior de Idade')
