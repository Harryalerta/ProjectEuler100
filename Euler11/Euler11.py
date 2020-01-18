gridfile = open('Euler11Data', 'r')

grid=[]

for i in range(0, 20):
    grid.append([])
    for j in range (0,20):
        grid[i].append(int(gridfile.read(2)))
        gridfile.read(1)

greater = 0
for i in range(0, 20):
    for j in range(0, 20):
        if i < 17:
            product = 1
            for k in range (0, 4):
                product *= grid[i + k][j]
            if product > greater:
                greater = product
        if j < 17:
            product = 1
            for k in range (0, 4):
                product *= grid[i][j+k]
            if product > greater:
                greater = product
        if i < 17 and j < 17:
            product = 1
            for k in range (0, 4):
                product *= grid[i + k][j + k]
            if product > greater:
                greater = product
        if i < 17 and j > 2:
            product = 1
            for k in range (0, 4):
                product *= grid[i + k][j - k]
            if product > greater:
                greater = product

print(greater)



