''' DESCRIÇÃO DO DESAFIO
Indicar o número de elementos faltantes em um vetor de numeros naturais onde:
'''


def makeArrayConsecutive2(statues):

    statues.sort()
    faltantes = []
    n = 0
    x1 = statues[0]
    x2 = statues[-1]
    lista = range(x1, x2 + 1)

    for i in lista:
        while n < len(statues):
            if i == statues[n]:
                n += 1
                break
            else:
                faltantes.append(i)
                break
    numero = len(faltantes)
    return numero


# teste - input: [4, 7] | output: 2
x = [4, 7]
print(makeArrayConsecutive2(x))
