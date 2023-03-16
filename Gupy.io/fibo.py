# Definindo o número a ser verificado
num = 9

# Iniciando a sequência de Fibonacci com 0 e 1
fib = [0, 1]

# Loop para calcular a sequência até que o último número seja maior ou igual ao número a ser verificado
while fib[-1] < num:
    # Adicionando o próximo número da sequência como a soma dos 2 anteriores
    fib.append(fib[-1] + fib[-2])

# Verificando se o número está na sequência
if num in fib:
    print(f"O número {num} pertence à sequência de Fibonacci: {fib}")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci: {fib}")
