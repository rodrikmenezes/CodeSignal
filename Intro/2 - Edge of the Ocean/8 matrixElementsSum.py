# =============================================================================
# DESCRIÇÃO DO DESAFIO
# Somar todos os valores que não aparecem acima de um 'zero' da matriz fornecida
# =============================================================================

# output: 9
matrix = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]

x = len(matrix)
y = len(matrix[0])
zeros = []
soma_total = 0
soma_zeros = 0
for i in range(1, x):
        
        for j in range(y):
            soma_total += matrix[i][j]
            if matrix[i-1][j] == 0:
                print(matrix[i][j])
                zeros.append(j)
                soma_zeros += matrix[i][j]

#for i in range(1, len(matrix)):
#    for j in matrix[i]:
#        if matrix[i-1] != 0:
#            print(j)