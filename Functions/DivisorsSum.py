def divisorslist(factorization):
    def addtocombinations():
        combinations[lenght-1] += 1
        for i in range(lenght-1,1,-1):
            if combinations[i] == factorization[i][1]:
                combinations[i-1] += 1
                combinations[i] = 0
        if combinations[0] == factorization[0][1]:
            saida = 1
        return

    divisorslist = []
    combinations = []
    lenght = factorization.__len__()
    for i in range(1, lenght):
        combinations.append(0)
    saida = 0
    while saida == 0:
        addtocombinations()
        divisor = 1
        for i in range(0, lenght-1):
            divisor = divisor * (factorization[i][0]**combinations[i])
        divisorslist.append(divisor)
