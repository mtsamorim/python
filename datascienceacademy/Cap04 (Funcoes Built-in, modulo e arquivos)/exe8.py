# Exercício 8 - Considere o código abaixo. Obtenha o mesmo resultado usando o pacote time. 
# Não conhece o pacote time? Pesquise!
#import datetime
import time
from time import strftime

#print (datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))

strftime('%d/%m/%Y %H:%M', time.localtime())