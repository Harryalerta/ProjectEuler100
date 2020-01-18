def searchprimeuntil(teto):
    listprimes = []
    for i in range(2, teto):
        listprimes.append(i)
    for i in listprimes:
        for testindex in range(i * 2, teto, i):
            if listprimes.__contains__(testindex):
                listprimes.remove(testindex)
    return listprimes


lista = searchprimeuntil(150000)
printfile = open("../Data/primeslist.txt", "w")
for i in lista:
    print(i, file=printfile)
    print(i)
printfile.close()
