# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

day = input("Qual o dia da semana?")
day = day.capitalize()

if day == "Domingo" or day == "Sabado":
    print("Hoje é dia de descanso")
else:
    print("Você precisa Trabalhar!")