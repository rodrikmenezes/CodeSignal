''' DESCIÇÃO DO DESAFIO
Given an array of integers, find the pair of adjacent elements that 
has the largest product and return that product
'''

def adjacentElementsProduct(inputArray):
    ''' (list) -> int
    Esta função devolve o maior produto entre dois elementos adjacentes de inputArray
    '''
    i = 1
    produto = []
    while i < len(inputArray):
        produto.append(inputArray[i] * inputArray[i - 1])
        i += 1
    maximo_produto = max(produto)

    return maximo_produto

### testes ###
def testes():
    # Arrays para teste. O vetorRespsta contém o respectivo resultado esperado
    inputArray = [[5, 6, -4, 2, 3, 2, -23], [9, 5, 10, 2, 24, -1, -48], [4, -6, 18, 7, 3, 53]]
    vetorResposta = [30, 50, 159]
    quantidade_de_testes = len(inputArray)

    for i in range(quantidade_de_testes):
        if adjacentElementsProduct(inputArray[i]) == vetorResposta[i]:
            print('OK para: ', inputArray[i])
        else:
            print('ERRO para', inputArray[i], '. Valor esperado: ', vetorResposta[i])

# iniciar testes
testes()