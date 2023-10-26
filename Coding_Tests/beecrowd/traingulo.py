meas = [float(x) for x in input().split()]

a = meas[0]
b = meas[1]
c = meas[2]
ab = a+b
ac = a+c
cb = c+b

if ab>c and ac>b and cb>a:
    per = a + b + c
    print(f'Perimetro = {per:.1f}')
else:
    area = ((a+b)/2)*c
    print(f'Area = {area:.1f}')
