"""
PEP8 - Python Enhancement Proposal

São Propostas de melhoria para a linguagem pyhton

The Zen of Python

import this

[1] - Utilize Camel Case para nomes de classe
class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minúsculo, separados de underline para funções ou variáveis
def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5


[3] - Sempre use 4 spaces para a identação!!! (Preste atenção se o TAB está configurado pra 4 spaces)

if 'a' in ' banana':
    print('tem') 

[4] - Linhas em Branco
- Separar funções e definições  de classe  com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports devem ser sempre feitos em linhas separadas;
# Import Errado

import sys, os

# Import Certo

import sys
import os

# Não há problemas em usar:
from types import StringType, ListType

#Caso tenha que fazer muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports sempre devem ser colocados no topo do arquivo, logo depois de comentários ou docstrings e antes de 
# variáveis e antes de constantes

[6] - Espaços em expressões e instruções
# Não Faça
funcao( algo[ 1], { outro: 2 })

# Faça
funcao(algo[1], {outro: 2})

# Não Faça:
algo (1)

# Faça:
algo(1)

# Não Faça:
dict ['chave'] = lista [indice]

# Faça:
dict['chave'] = lista[indice]



"""