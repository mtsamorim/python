values = [float(x) for x in input().split()]

for x in range(int(len(values))-1):
    for x in range(int(len(values))-1):
        if values[x] < values[x+1]:
            aux = values[x]
            values[x] = values[x+1]
            values[x+1] = aux

a = values[0]
b = values[1]
c = values[2]

if( a>=b+c):
    print('NAO FORMA TRIANGULO')
elif((a*a)==(b*b)+(c*c)):
    print('TRIANGULO RETANGULO')
elif((a*a)>(b*b)+(c*c)):
    print('TRIANGULO OBTUSANGULO')
elif((a*a)<(b*b)+(c*c)):
    print('TRIANGULO ACUTANGULO')
if(a==b and a==c):
    print('TRIANGULO EQUILATERO')
elif(a==b or b==c or c==a):
    print('TRIANGULO ISOSCELES')
