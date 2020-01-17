data = open('Euler08data', 'r')
digitslist = []
for i in range(0,20):
    line = data.read(50)
    data.read(1)
    for c in line:
        digitslist.append(int(c))
greatest = 0
for i in range(0,987):
    product = 1
    for j in range(0,13):
        product *= digitslist[i+j]
    if product > greatest:
        greatest = product
print(greatest)
