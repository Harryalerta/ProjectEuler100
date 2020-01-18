numberfile = open('Euler13Data', 'r')
numbers=[]
for i in range (0, 100):
    numbers.append(numberfile.read(50))
    numberfile.read(1)

sum = 0

for i in range(49, 25, -1):

    for j in range(0, 100):
        sum += int(numbers[j][i])
    sum = int(sum/10)

for i in range(0, 100):
    sum+= int(numbers[i][0:26])

print(sum)