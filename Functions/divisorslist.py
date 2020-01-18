from Functions import factorization


def divisorslist(number):
    factors = factorization.factorization(number)
    list = [1]
    combinations = []
    lenght = factors.__len__()
    for i in range(0, lenght):
        combinations.append(0)
    saida = 0
    while saida == 0:
        combinations[-1] += 1
        for i in range(lenght - 1, 0, -1):
            if combinations[i] == factors[i][1] + 1:
                combinations[i - 1] += 1
                combinations[i] = 0
        if combinations[0] == factors[0][1] + 1:
                return list
        divisor = 1
        for i in range(0, lenght):
            divisor *= (factors[i][0]**combinations[i])
        list.append(divisor)
