values = [int(x) for x in input().split()]
time = []

start = values[0]
final = values[1]
aux = start
count = 0
x = True

for x in range(24):
    time.append(int(x))

while(x):
    if aux > 23:
        aux = 0    

    if time[aux] == final:
        x = False
    else:
        aux = aux + 1
        count = count + 1

if start == final:
    print(f'O JOGO DUROU {24} HORA(S)')
else:
    print(f'O JOGO DUROU {count} HORA(S)')
