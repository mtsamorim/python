def calcN(a, b, c, d):

    aux = (a*2 + b*3 + c*4 + d)/(2+3+4+1)

    return aux

notes = [float(x) for x in input().split()]

average = calcN(notes[0], notes[1], notes[2], notes[3]) 

if average >= 7.0:
    print(f'Media: {average:.1f}')
    print('Aluno aprovado.')
elif average >= 5.0 and average <= 6.9:
    print(f'Media: {average:.1f}')
    print('Aluno em exame.')
    aux = float(input())
    aux1 = (aux + average)/2

    if aux1 >= 5.0:
        print(f'Nota do exame: {aux:.1f}')
        print('Aluno aprovado.')
        print(f'Media final: {aux1:.1f}')
    else:
        print(f'Nota do exame: {aux:.1f}')
        print('Aluno reprovado.')
        print(f'Media final: {aux1:.1f}')
else:
    print(f'Media: {average:.1f}')
    print('Aluno reprovado.')
