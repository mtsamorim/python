import random
import re

#list with the gallows formated
gallows = [
"""
++++++++++++ THE HANGMAN GAME ++++++++++++

 ------- 
 |     |
       |
       |
       |
       |
    ======

""",
"""

 ------- 
 |     |
 O     |
       |
       |
       |
    ======

""",
"""
 ------- 
 |     |
 O     |
 |     |
       |
       |
    ======

""",
"""
 ------- 
 |     |
 O     |
/|     |
       |
       |
    ======

""",
"""
 ------- 
 |     |
 O     |
/|\    |
       |
       |
    ======

""",
"""
 ------- 
 |     |
 O     |
/|\    |
/      |
       |
    ======

""",
"""
 ------- 
 |     |
 O     |
/|\    |
/ \    |
       |
    ======

""",
"""
 ------- 
 |     |
 º     |
/|\    |
/ \    |
       |
    ======

"""]


class Hangman:
    # Constructor method
    def __init__(self, word):
        self.word = word
        self.ml = []
        self.cl = []
        self.gl = []
        self.aux = []
        self.aux1 = False 
        self.aux2 = 0
        for x in range(len(self.word)):
            self.gl.append(' _ ')

        for x in range(len(self.word)):
            self.aux.append(self.word[x])

        

        
        
    # Método para adivinhar a letra
    def guess(self,letter):
        aux3 = False
        word3 = ' '.join(str(x) for x in self.ml)
        word4 = ' '.join(str(x) for x in self.cl)
        for x in range(len(self.word)):
            if letter == self.aux[x]:
                self.gl[x] = letter
                if letter not in word4:
                    self.cl.append(letter)
                aux3 = True

        if aux3 == False and letter not in word3:
            if letter not in word3:
                self.ml.append(letter)
            
            
            self.aux2 = self.aux2 + 1

        
    # Método para verificar se o jogo terminou
    def hangmanover(self):
        bo = self.hangmanwon()
        if bo == True:
            return True
        elif self.aux2 == 7:
            return True
        elif bo == False:
            return False
        
    # Método para verificar se o jogador venceu
    def hangmanwon(self):
        aux4 = True
        x = 0
        while x < len(self.word):
            if self.gl[x] == ' _ ':
                aux4 = False
            
            x = x +1

        return aux4

    # Método para não mostrar a letra no board
    def hide_word(self):
        for x in range(len(self.word)):
            self.gl = []

    # Método para checar o status do game e imprimir o board na tela
    def status(self):
        word = ' '.join(str(x) for x in self.gl)

        word1 = ' '.join(str(x) for x in self.ml)

        word2 = ' '.join(str(x) for x in self.cl)

        return print(gallows[self.aux2] +"\nLetras Erradas: "+ word1.upper() +"\n\nLetras Certas: "+ word2.upper() +"\n\nPalavra: " + word.upper() + "\n\n")
         

# Function to get random word
def randword():
    with open("C:\\Users\malva\Documents\GitHub\python\projects\HagmanGame\words.txt", "r") as file:
        allText = file.read()
        words = [str(x) for x in allText.split()]

    return random.choice(words)

# Function Main
def main():
    
    # Objeto
    forca1 = Hangman(str(randword()))

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not forca1.hangmanover():
        forca1.status()
        user_letter = input("Type a letter: ")
        aux = False
        
        while user_letter.isalpha() == False:
            user_letter = input("\nType a Valid letter: ")
            
        forca1.guess(user_letter)
    
    # De acordo com o status, imprime mensagem na tela para o usuário
    if forca1.hangmanwon():
        forca1.status()
        print ('\nParabéns! Você venceu!!')
    else:
        forca1.status()
        print ('\nGame over! Você perdeu.')
        print ('A palavra era ' + forca1.word)       


main()
