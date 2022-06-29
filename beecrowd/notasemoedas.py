def money(x):
    n100 = int(x/100)
    aux = x%100
    n50 = int(aux/50)
    aux = aux%50
    n20 = int(aux/20)
    aux = aux%20
    n10 = int(aux/10)
    aux = aux%10
    n5 = int(aux/5)
    aux = aux%5
    n2 = int(aux/2)
    aux = aux%2
    c1 = int(aux/1)
    aux = aux%1
    c50 = int(aux/0.50)
    aux = aux%0.50
    c25 = int(aux/0.25)
    aux = aux%0.25
    c10 = int(aux/0.10)
    aux = aux%0.10
    c05 = int(aux/0.05)
    aux = aux%0.05
    c01 = int(aux/0.01)

    return print("NOTAS:\n%i nota(s) de R$ 100.00\n%i nota(s) de R$ 50.00\n%i nota(s) de R$ 20.00\n%i nota(s) de R$ 10.00\n%i nota(s) de R$ 5.00\n%i nota(s) de R$ 2.00\nMOEDAS:\n%i moeda(s) de R$ 1.00\n%i moeda(s) de R$ 0.50\n%i moeda(s) de R$ 0.25\n%i moeda(s) de R$ 0.10\n%i moeda(s) de R$ 0.05\n%i moeda(s) de R$ 0.01" %(n100, n50, n20, n10, n5, n2, c1, c50, c25, c10, c05, c01))


din = float(input())

money(din)
