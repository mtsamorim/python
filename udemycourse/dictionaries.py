"""
Dicionarios

1 - Dicionarios são coleções tipo chave/valor 
2 - Dicionarios são declarados por {}

OBS:
- Pode misturar os tipos de dados
- tanto chave quanto valor pode ser de qualque tipo de dado

#Criando um dicionario FORMA 1 (mais utilizavel)

paises = {'br':'Brasil', 'usa':'United States', 'ar':'Argentina'}

print(paises)
print(type(paises))


#FORMA 2 (Menos comum)

paises2 = dict(br='Brasil', usa='United States', ar='Argentina')

print(paises2)
print(type(paises2))
"""

#Adicionar elementos em um dicionario 
meses = {'jan':100, 'fev':200, 'mar':300}
print(meses)

#forma 1

meses['abr'] = 400
print(meses)

#forma 2
new_date = {'mai':500}

meses.update(new_date) #poderia fazer meses.update({'mai':500})
print(meses)

#Atualizando elementos do dicionario

