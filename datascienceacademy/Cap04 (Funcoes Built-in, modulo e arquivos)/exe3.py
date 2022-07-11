# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
def matrixT(x):
    matrixA = []
    matrixB = []
    matrixT = []
    
    for i, y in matrix:
        matrixA.append(i)
        matrixB.append(y)
        
    matrixT.append(matrixA)
    matrixT.append(matrixB)
        
    return matrixT

matrix = [[1, 2],[3,4],[5,6],[7,8]]
    
for i in matrixT(matrix):
    print(i)