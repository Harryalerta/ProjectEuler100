primesfile = open('primeslist.txt', 'r+')

primeslist = []
prime = int(primesfile.readline())
primeslist.append(prime)
while prime != '':
    prime = primesfile.readline()
    if prime != '':
        prime=int(prime)
        primeslist.append(prime)
numbertotest = primeslist[-1] + 2

numbertotest = 0
while numbertotest < 20000:
    isprime = 1
    tester = 0
    for tester in primeslist and tester < numbertotest**0.5 and isprime == 1:
        if numbertotest % tester == 0:
            isprime = 0
    if isprime == 1:
        primeslist.append(numbertotest)
        print(numbertotest, file=primesfile)