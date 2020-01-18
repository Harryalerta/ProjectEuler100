from Functions import divisorscount
DivisorsCount = 0
index = 2
triangleNumber = 1
while DivisorsCount < 500:
    triangleNumber += index
    DivisorsCount = divisorscount.divisorscount(triangleNumber)
    index += 1

print(triangleNumber)