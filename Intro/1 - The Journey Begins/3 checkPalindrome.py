# =============================================================================
# DESCRIÇÃO DO PROBLEMA
# Given the string, check if it is a palindrome
# A palindrome is a string that reads the same left-to-right and right-to-left
# =============================================================================


def checkPalindrome(inputString):

    """ (str) -> boolean
    Verifica se o reverso do parâmetro é a mesma palavra
    """

    x_len = len(inputString)

    if x_len % 2 == 0:
        metade = int(x_len / 2)
        if inputString[:metade] == inputString[-metade:][::-1]:
            resultado = True
        else:
            resultado = False
    else:
        metade = int(round(x_len / 2))
        if inputString[:metade] == inputString[-metade:][::-1]:
            resultado = True
        elif metade == 0:
            resultado = True
        else:
            resultado = False

    return resultado

### TESTES ###
def testes():
    # Arrays para teste. O vetorRespsta contém o respectivo resultado esperado
    strings_teste = ['atta', 'awuwa', 'a', 'AffA', 'A', 'qwe']
    vetorResposta = [True, True, True, True, True, False]
    quantidade_de_testes = len(strings_teste)
    for i in range(quantidade_de_testes):
        if checkPalindrome(strings_teste[i]) == vetorResposta[i]:
            print('OK para o teste com: ', strings_teste[i])
        else:
            print('ERRO para o teste com: ', strings_teste[i])

# executar testes
testes()
