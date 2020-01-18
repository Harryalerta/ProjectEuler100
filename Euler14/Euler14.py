def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return number * 3 + 1


bigger = [0, 0]
for i in range(1, 1000000):
    chain = 0
    entry = i
    while entry != 1:
        entry = collatz(entry)
        chain += 1
    if chain > bigger[0]:
        bigger = [chain, i]

print(bigger[1])