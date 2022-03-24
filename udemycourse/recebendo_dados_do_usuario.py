"""
recebendo dados do usuário

input() -> Todo valor recebecido via input é do tipo string
"""

# Entrada de Dados
print("Qual o seu nome?")
nome = input()

# Exemplo de print 'antigo' 2.x
# print('Seja Bem-Vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja Bem-Vindo(a) {0}' .format(nome))

# Exemplo de print 'mais atual' 3.7
print (f'Seja Bem-Vindo(a) {nome}')

print("Qual a sua idade?")
idade = input()

# Exemplo de print 'antigo' 2.x
# print('A %s tem %s ano(s)' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('O {0} tem {1} ano(s)' .format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print (f'O(a) {nome}  tem {idade} ano(s)')

print(f'O(a) {nome} nasceu em {2022 - int(idade)}')
