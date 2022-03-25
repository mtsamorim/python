"""
Tipo String 
"""

nome = 'Matheus'
print(nome)
print(type(nome))

nome = "Amorim"
print(nome)
print(type(nome))

nome = '''Jorge'''
print(nome)
print(type(nome))

teste = 'abacaxi'
print(teste.upper())

teste = 'ABACAXI'
print(teste.lower())

# Transforma em uma Lista de Strings
teste = 'Matheus Amorim'
print(teste.split())

teste = 'Matheus Amorim'
print(teste[0])

print(teste[0:3])

print(teste[::-1])

print(teste.replace('a', 'X'))