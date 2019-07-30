# =============================================================================
# DESCRIÇÃO DO DESAFIO
# Somar todos os valores que não aparecem acima de um 'zero' da matriz fornecida
# =============================================================================


import numpy as np

def matrixElementsSum(matrix):
    
    matrix_clone = matrix[:]
    x = len(matrix)
    y = len(matrix[0])
    
    for i in range(1, x):
        for j in range(y):
            if matrix[i-1][j] == 0:
                matrix_clone[i][j] = 0
    
    matrix_final = np.array(matrix_clone)
    return sum(sum(matrix_final))


# TESTES

testes = [0] * 2
resultados_esperados = [0] * 2
respostas = []
comparacao = []

testes[0] = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
resultados_esperados[0] = 9

testes[1] = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]
resultados_esperados[1] = 9

n = 0
for teste in testes:
    respostas.append(matrixElementsSum(teste))
    if respostas[n] == resultados_esperados[n]:
        comparacao.append('OK')
    else:
        comparacao.append('ERRO!')    
    print('teste', n+1,'- resultado esperado:', resultados_esperados[n],
          '  resultado do programa:', respostas[n], comparacao[n])
    n += 1