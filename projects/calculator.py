def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x,y):
        return x / y

print("+++++++++++++++++++Python Calculator+++++++++++++++++++\n")

opt = int(input("Seleciona o número da opção desejada: \n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\nDigite sua opção [1/2/3/4]: "))

if(opt == 1 or opt == 2 or opt == 3 or opt == 4):
    
    num1 = input("\nDigite o primeiro número: ")
    
    num2 = input("\nDigite o segundo número: ")

    ty  = False

    for i in num1:
        if i == ".":
            ty = True

    num1 = float(num1)
    num2 = float(num2)

    if ty == True:
        if(opt == 1):
            print("\n%.1f + %.1f = %.1f" %(num1, num2, soma(num1, num2)))
        elif(opt == 2):
            print("\n%.1f - %.1f = %.1f" %(num1, num2, sub(num1, num2)))
        elif(opt == 3):
            print("\n%.1f * %.1f = %.1f" %(num1, num2, mul(num1, num2)))
        else:
            print("\n%.1f / %.1f = %.1f" %(num1, num2, div(num1, num2)))
    else:
        if(opt == 1):
            print("\n%.0f + %.0f = %.0f" %(num1, num2, soma(num1, num2)))
        elif(opt == 2):
            print("\n%.0f - %.0f = %.0f" %(num1, num2, sub(num1, num2)))
        elif(opt == 3):
            print("\n%.0f * %.0f = %.0f" %(num1, num2, mul(num1, num2)))
        else:
            if num2 != 0:               
                    print("\n%.0f / %.0f = %.1f" %(num1, num2, div(num1, num2)))
            else:
                try:
                    div(num1, num2)
                except ZeroDivisionError:
                    print("\nOperação Indefinida, por favor escolha um novo divisor.")
                 
else:
    print("\nOpção Inválida")