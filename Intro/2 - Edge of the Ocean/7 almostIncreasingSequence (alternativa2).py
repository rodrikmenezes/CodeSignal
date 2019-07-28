def almostIncreasingSequence(sequence):
    f1 = sum([1 for a, b in zip(sequence[:-1], sequence[1:]) if a>=b ]) <= 1 
    f2 = sum([1 for a, c in zip(sequence[:-2], sequence[2:]) if a>=c ]) <= 1
    return f1 and f2




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

