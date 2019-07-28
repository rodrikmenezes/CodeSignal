# =============================================================================
# DESCRIÇÃO DO DESAFIO
# Given a year, return the century it is in. The first century spans
# from the year 1 up to and including the year 100, the second - from the
# year 101 up to and including the year 200, etc
# =============================================================================


def centuryFromYear(year):

    seculo = (year % 1000) // 100
    x_str = str(year)

    if year < 1000:
        if x_str[-2:] == '00':
            return seculo
        else:
            seculo = seculo + 1
    else:
        if x_str[-2:] == '00':
            seculo = int(x_str[:2])
        else:
            seculo = int(x_str[:2]) + 1
    return seculo


# TESTE #
# este teste mostra o que o algorítimo retorna do ano 0 ao ano 1900,
# em intervalos de 100 anos

for i in range(1, 3000, 100):
    print('Para o ano %d -> Século %d' % (i - 1, centuryFromYear(i - 1)))
    print('Para o ano %d -> Século %d' % (i, centuryFromYear(i)))
