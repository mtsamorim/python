number = float(input())

if number >=0 and number <= 25.0000:
    print("Intervalo [0,25]")
elif number > 25.0000 and number <= 50.0000000:
    print("Intervalo (25,50]")
elif number > 50.0000000 and number <= 75.0000000:
    print("Intervalo (50,75]")
elif number > 75.0000000 and number <= 100.0000000:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
    