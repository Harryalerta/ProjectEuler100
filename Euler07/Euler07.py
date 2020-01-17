primeslist = open("primeslist.txt", "r")
for i in range(0, 10001):
    answer = primeslist.readline()
print(answer)
primeslist.close()