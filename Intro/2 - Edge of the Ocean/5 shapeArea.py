# =============================================================================
# DESCRIÇÃO DO DESAFIO
# O desafio é escrever uma função onde se recebe como input um número natural
# e como output a área correspondente
# que descrita pela figura area areaShape.png em anexo
# =============================================================================


def shapeArea(n):
    lateral = n + (n - 1)
    soma = lateral
    while lateral > 1:
        lateral = lateral - 2
        soma = soma + 2 * lateral
    return soma

### TESTES ###
def testes():
    n = [1,2,3,4]
    vetorResposta = [1,5,13,25]
    for i in range(len(n)):
        if shapeArea(n[i]) == vetorResposta[i]:
            print('OK para: ', n[i])
        else:
            print('ERRO para: ', n[i], '. Valor esperado: ', vetorResposta[i])

# executar testes
testes()
