def test(x):
    if x[1] > x[2] and x[3] > x[0] and x[2]+ x[3] > x[0] + x[1] and x[2] >= 0 and x[3] >= 0:
        return True
    else:
        return False

list1 = []

list1 = list(map(int, input().split()))

if test(list1) == True:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")