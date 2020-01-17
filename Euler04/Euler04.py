def ispalindrome(number):
    string = str(number)
    answer = 1
    for i in range (0, int(string.__len__()/2)):
        if string[i] != string[-i-1]:
            answer = 0
    return answer


largest = 0
for i in range (100,999):
    for j in range(100,999):
        if i*j > largest and ispalindrome(i*j) == 1:
            largest = i*j

print(largest)