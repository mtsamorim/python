import random
from dataclasses import dataclass

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

"""]

@dataclass
class Hangman:

    word = str

    def guess(self, letter):
        for i in self.word:
            return print(i)


def randword():
    with open("C:\\Users\malva\Documents\GitHub\python\projects\Hagman Game\words.txt", "r") as file:
        allText = file.read()
        words = [str(x) for x in allText.split()]

    return random.choice(words)

def main():
    aux = randword()
    forca1 = Hangman(aux)
    #return print(aux)

main()
