piramidfile = open('Euler67data.txt', 'r')


def cutlevel(first, second):
    for k in range(0, len(first) - 1):
        if first[k] > first[k + 1]:
            second[k] += first[k]
        else:
            second[k] += first[k + 1]
    return second


piramid = []
for i in range(0, 15):
    piramid.append([])
    for j in range(0, i + 1):
        piramid[i].append(int(piramidfile.read(2)))
        piramidfile.read(1)

piramid.reverse()

for j in range(0, 14):
    piramid[j + 1] = cutlevel(piramid[j], piramid[j + 1])

print(piramid[14])
