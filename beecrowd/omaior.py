a, b ,c = input().split(' ')

a = int(a)
b = int(b)
c = int(c)

maiorABC = int((a+b+abs(a-b))/2)

if maiorABC > c:
    print(f'{maiorABC} eh o maior')
else:
    print(f'{c} eh o maior')
    