def time(x):
    s = x%60
    aux = x/60
    m = 0
    h = 0
    if aux < 60:
        m = aux
    else:
        h = aux/60
        m = aux%60
    
    return print("%i:%i:%i" %(h, m, s))

sec = int(input())

time(sec)
