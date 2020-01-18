from Functions import factorization

list = [[2, 1]]
for i in range(2,21):
    factors = factorization.factorization(i)
    newprime = 1
    for j in factors:
        for k in list:
            if k[0] == j[0]:
                newprime=0
                if j[1] > k[1]:
                    k[1] = j[1]
    if newprime == 1:
        list.append(j)
anwser = 1
for i in list:
    anwser *= i[0]**i[1]
print(anwser)