from Functions import factorization

def divisorscount(number):
    count = 1
    factors = factorization.factorization(number)
    for i in factors:
        count *= i[1]+1
    return count