def allLongestStrings(inputArray):
    m = max(len(s) for s in inputArray)
    r = [s for s in inputArray if len(s) == m]
    return r


 
# TESTES

# teste 1 - output: ["aba", "vcd", "aba"]
inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print('teste 1 - ', allLongestStrings(inputArray))

# teste 2 - output: ['rodrick', 'claudio']
inputArray = ['rodrick', 'claudio', 'erik', 'pablo']
print('teste 2 - ', allLongestStrings(inputArray))

