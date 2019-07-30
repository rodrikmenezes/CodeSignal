# =============================================================================
# DESCRIÇÃO DO DESAFIO
# Given two strings, find the number of common characters between them.
# =============================================================================

def commonCharacterCount(s1, s2):

    contador = 0
    
    for letra_s1 in s1:
        for letra_s2 in s2:
            if letra_s1 == letra_s2:
                contador += 1
                s2 = s2.replace(letra_s2, '', 1)
                s1 = s1.replace(letra_s1, '', 1)
                break
    return contador
            
# TESTES

# teste1 - output: 3
s1 = "aabcc"
s2 = "adcaa"

print('teste 1:', commonCharacterCount(s1, s2))