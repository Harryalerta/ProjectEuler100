def divisorslist(factorization):
    list = []
    combinations = []
    lenght = factorization.__len__()
    print(lenght)
    for i in range(0, lenght):
        combinations.append(0)
    print(combinations)
    saida = 0
    while saida == 0:
        print('loop')
        combinations[-1] += 1

        for i in range(lenght - 1, 0, -1):
            if combinations[i] == factorization[i][1] + 1:
                combinations[i - 1] += 1
                combinations[i] = 0
        if combinations[0] == factorization[0][1] + 1:
                return list
        divisor = 1
        for i in range(0, lenght):
            divisor *= (factorization[i][0]**combinations[i])
        print(combinations)
        list.append(divisor)
