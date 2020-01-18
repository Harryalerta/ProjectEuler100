primesfile = open('../Data/primeslist.txt', 'r+')

primeslist = []
prime = int(primesfile.readline())
primeslist.append(prime)
while prime != '':
    prime = primesfile.readline()
    if prime != '':
        prime=int(prime)
        primeslist.append(prime)
numbertotest = primeslist[-1] + 2
print(numbertotest)

while numbertotest < 2000000:
    isprime = 1
    tester = 2
    upperlimit = numbertotest**0.5
    index = 1
    while tester < upperlimit and isprime == 1:
        tester = primeslist[index]
        if numbertotest % tester == 0:
            isprime = 0
        index += 1
    if isprime == 1:
        primeslist.append(numbertotest)
        print(numbertotest, file=primesfile)
    numbertotest += 2

sum = 0
for i in primeslist:
    sum += i

print(sum)