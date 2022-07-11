import math

def bhask(a,b,c):

    aux3 = False
    delta = (b*b) - 4*a*c
    
    if delta <=0:
        aux3 = True
    else:
        aux1 = (-b + math.sqrt(delta))/(2*a)
        aux2 = (-b - math.sqrt(delta))/(2*a)

    return aux1, aux2, aux3


list1 = [float(x) for x in input().split()]

if list1[1]*list1[1] - 4*list1[0]*list1[2] >= 0:
    if list1[0] != 0:
        r1, r2, sta = bhask(list1[0],list1[1],list1[2])

        if sta == False:
            print(f'R1 = {r1:.5f}')
            print(f'R2 = {r2:.5f}')
        else:
            print("Impossivel calcular")
    else:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")
