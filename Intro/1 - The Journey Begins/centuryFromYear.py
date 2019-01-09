def centuryFromYear(year):


    seculo = 0
    milenio = year // 1000
    seculo = (year % 1000) // 100
    decada = (year % 100) // 10

    x_str = str(year)
    # print(len(x_s))

    if year < 1000:
        if x_str[-2:] == '00':
            seculo = seculo
        else:
            seculo = seculo + 1
    else:
        if x_str[-2:] == '00':
            seculo = int(x_str[:2])
        else:
            seculo = int(x_str[:2]) + 1
    return seculo


# Teste
for i in range(1, 3000, 100):
    print('Para o ano %d = %d' % (i - 1, centuryFromYear(i - 1)))
    print('Para o ano %d = %d' % (i, centuryFromYear(i)))
