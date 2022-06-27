value = int(input())
valueback = value
list1 = [100, 50, 20, 10, 5, 2, 0]

for i in range(0, 6):
    div = int(list1[i])
    list1[i] = int(value/div)
    value = value%div

if value != 0:
    list1[6] = 1

print(valueback)
print(f'{list1[0]} nota(s) de R$ 100,00')
print(f'{list1[1]} nota(s) de R$ 50,00')
print(f'{list1[2]} nota(s) de R$ 20,00')
print(f'{list1[3]} nota(s) de R$ 10,00')
print(f'{list1[4]} nota(s) de R$ 5,00')
print(f'{list1[5]} nota(s) de R$ 2,00')
print(f'{list1[6]} nota(s) de R$ 1,00')