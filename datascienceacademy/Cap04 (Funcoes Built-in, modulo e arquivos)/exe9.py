# Exercício 9 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
def changevalue(d1, d2):
    dictaux = {}
    dictaux = dict(zip(d1, d2.values()))
    
    return dictaux

dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}
dict3 = {}

dict3 = changevalue(dict1, dict2)

print(dict3)