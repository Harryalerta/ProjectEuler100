def factorization(number):
    if number < 2:
        return 1
    factorizationlist = []
    primeslist = open("../Data/primeslist.txt", "r")
    primeread = primeslist.readline()
    primetotest = int(primeread)
    while number > 1:
        if number % primetotest == 0:
            number = int(number / primetotest)
            if factorizationlist.__len__() == 0 or factorizationlist[-1][0] != primetotest:
                factorizationlist.append([primetotest, 1])
            else:
                factorizationlist[-1][1] += 1
        else:
            primeread = primeslist.readline()
            primetotest = int(primeread)
    primeslist.close()
    return factorizationlist
