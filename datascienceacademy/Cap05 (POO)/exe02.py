# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    cidade: str
    telefone: str
    email: str
    altura: str
    
    def __str__(self):
        return f'Nome: {self.nome}\nCidade: {self.cidade}\nTelefone: {self.telefone}\nemail: {self.email}\nAltura: {self.altura}'

people1 = Pessoa('Oswaldo', 'Rio de Janeiro', '21992954678', 'oswaldo@gmail.com', '1.78')

print(people1)

"""hasattr(people1, "altura")"""

del people1.altura
hasattr(people1, "altura")
