# =============================================================================
# DESCRIÇÃO DO DESAFIO
# Given a sequence of integers as an array, determine whether it is possible
# to obtain a strictly increasing sequence by removing no more than one element
# from the array
# =============================================================================


def almostIncreasingSequence(sequence):
    
    # variáveis auxiliares
    posicao = []
    tamanho = len(sequence)
    resultado_parcial = []
    
    # looping que captura a posição de valores discrepantes (quebram a sequência)
    n = 0
    while n < tamanho - 1:
        if sequence[n + 1] < sequence[n]:
            posicao.append(n)
            posicao.append(n + 1)
        n += 1
    
    # se não existem valores que quebram a sequência, resposta = False
    if posicao == []:
        resultado = False
    
    # caso especial de vetor com apenas 2 elementos
    if len(sequence) == 2 and sequence[1] >= sequence[0]:
        resultado = True
    elif len(sequence) == 2 and sequence[1] < sequence[0]:
        resultado = False
    
    # looping que testa a sequência do vetor principal sem valores discrepantes
    t = 0
    while t < len(posicao):
        sequence_aux = sequence[:]
        sequence_aux.pop(posicao[t])
        tamanho_aux = len(sequence_aux)
        
        n = 0
        while n < tamanho_aux - 1:
            if sequence_aux[n + 1] > sequence_aux[n]:
                resultado = True
            else:
                resultado = False
                break
            n += 1
        resultado_parcial.append(resultado)
        t += 1
    
    for i in resultado_parcial:
        if i == True:
            resultado = True
    
    return resultado





# TESTES
teste = [0] * 11
resultado_esperado = [0] * 11

teste[0] = ([1, 3, 2])
resultado_esperado[0] = True

teste[1] = ([1, 3, 2, 1])
resultado_esperado[1] = False

teste[2] = ([1, 2, 1, 2])
resultado_esperado[2] = False

teste[3] = ([1, 1, 2, 3, 4, 4])
resultado_esperado[3] = False

teste[4] = ([1, 2, 3, 4, 3, 6])
resultado_esperado[4] = True

teste[5] = ([1, 1])
resultado_esperado[5] = True

teste[6] = ([10, 1, 2, 3, 4, 5])
resultado_esperado[6] = True

teste[7] = ([1, 2, 5, 3, 5])
resultado_esperado[7] = True

teste[8] = ([3, 6, 5, 8, 10, 20, 15])
resultado_esperado[8] = False

teste[9] = ([1, 2, 3, 4, 5, 3, 5, 6])
resultado_esperado[9] = False

teste[10] = ([3, 5, 67, 98, 3])
resultado_esperado[10] = True

# EXECUTAR TESTES
respostas_programa = []
comparacao = []
acertos, erros, q = 0, 0, 0
while q < len(teste):
    respostas_programa.append(almostIncreasingSequence(teste[q]))
    if respostas_programa[q] == resultado_esperado[q]:
        comparacao.append('OK')
        acertos += 1
    else:
        comparacao.append('FALHOU!')
        erros += 1
    print('teste', q, 'programa:', respostas_programa[q],
          '/ esperado:', resultado_esperado[q], '/', comparacao[q])
    q += 1
print('\nPercentual de acertos =', 100 * round(acertos / (acertos + erros),2))
