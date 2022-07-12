dict1 = {1:4.00, 2:4.50, 3:5.00, 4:2.00, 5:1.50}

list1 = [int(x) for x in input().split()]

aux = float(dict1[list1[0]])
aux = aux * list1[1]

print(f'Total: R$ {aux:.2f}')
