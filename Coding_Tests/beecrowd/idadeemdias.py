def age(x):
    y = x/365
    aux = x%365
    m = aux/30
    d = aux%30
    
    return print("%i ano(s)\n%i mes(es)\n%i dia(s)" %(y, m, d))

days = int(input())

age(days)