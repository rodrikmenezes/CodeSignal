# =============================================================================
# DESCRIÇÃO DO DESAFIO
# Given an array of strings, return another array containing all of its longest strings.
# =============================================================================

def allLongestStrings(inputArray):
    
    contador = []
    lista_resposta = []
    
    for elemento in inputArray:
        contador.append(len(elemento))
    
    maximo = max(contador)
    
    for elemento in inputArray:
        if len(elemento) == maximo:
            lista_resposta.append(elemento)

    return lista_resposta

    
# TESTES

# teste 1 - output: ["aba", "vcd", "aba"]
inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print('teste 1 - ', allLongestStrings(inputArray))

# teste 2 - output: ['rodrick', 'claudio']
inputArray = ['rodrick', 'claudio', 'erik', 'pablo']
print('teste 2 - ', allLongestStrings(inputArray))

