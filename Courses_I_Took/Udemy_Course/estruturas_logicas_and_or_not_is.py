"""
Estruturas Lógicas: and, or, not , is

Operadores Unários:
    - not;
Operadores Binários:
    - and, or is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor booleano se inverte, se for True vira False, se for False vira True
"""

ativo = False
logado = True

if ativo and logado is True:
    print('Seja Bem-Vindo')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

if ativo and logado:
    print('Seja Bem-Vindo')

if ativo or logado:
    print('Seja Bem-Vindo')

if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

