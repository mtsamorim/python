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

    #def guess(self)


def randword():
    with open("C:\\Users\malva\Documents\GitHub\python\projects\Hagman Gamewords.txt", "r") as file:
        allText = file.read()
        words = [str(x) for x in allText.split()]

    return print(random.choice(words))

randword()