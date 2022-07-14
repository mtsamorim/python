# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.
from dataclasses import dataclass

@dataclass
class Smartphone:
    tamanho: str
    interface: str

@dataclass
class MP3Player(Smartphone):
    capacidade: str
        
    def print_MP3(self):
        return print(f'Tamanho: {self.tamanho}\nInterface: {self.interface}\nCapacidade: {self.capacidade}')

phone1 = MP3Player('pequeno', 'LCD','128 GB')

phone1.print_MP3()
