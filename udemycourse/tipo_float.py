"""
Tipo Float 

OBS: O separador de casa decimais na programação é o ponto e não a vírgula
# Errado
valor = 1,44

# Certo
valor = 1.44
"""
valor = 1, 44
print(type(valor))

valor = 1.44
print(type(valor))

valor1, valor2 = 1, 44
print(type(valor1))
print(type(valor2))

valor = 3.44
print(f'{int(valor)}')

valor = 5j
print(type(valor))
print(f'{valor**2}')

salario = 2.56
salario2 = 3.67

print(f'{salario + salario2}')
print(f'{int(salario) + int(salario2)}')