a, b ,c = input().split(' ')

a = float(a)
b = float(b)
c = float(c)

tri = a*c/2.0
cir = 3.14159*(c**2.0)
tra = ((a+b)*c)/2.0
qua = b**2.0
ret = a*b

print('TRIANGULO: {:.3f}' .format(tri))
print('CIRCULO: {:.3f}' .format(cir))
print('TRAPEZIO: {:.3f}' .format(tra))
print('QUADRADO: {:.3f}' .format(qua))
print('RETANGULO: {:.3f}' .format(ret))
