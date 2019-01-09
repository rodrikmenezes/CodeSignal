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

# Teste
print(checkPalindrome('atta'))
print(checkPalindrome('awuwa'))
print(checkPalindrome('a'))
print(checkPalindrome('AffA'))
print(checkPalindrome('A'))
print(checkPalindrome('qwe'))