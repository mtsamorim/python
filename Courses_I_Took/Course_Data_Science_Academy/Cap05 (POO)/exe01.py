# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, passando 2 parâmetros e depois faça uma chamada
# aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)

atlas = Rocket(123,6859)
scout = Rocket(13712,12398)

atlas.print_rocket()
scout.print_rocket()

atlas.move_rocket(100,-5000)
scout.move_rocket(-10000,10000)

atlas.print_rocket()
scout.print_rocket()