def letterscounting(number):
    count = 0
    hundreds = int(number/100)
    tenths = int((number % 100)/10)
    units = number % 10
    if hundreds == 10:
        # one thousand
        return 11
    if hundreds == 1:
        #one hundred and
        count += 13
    elif hundreds == 2:
        #two hundreds and
        count += 13
    elif hundreds == 3:
        #three hundreds and
        count += 15
    elif hundreds == 4:
        #four hundreds and
        count += 14
    elif hundreds == 5:
        #five hundreds and
        count += 14
    elif hundreds == 6:
        #six hundreds and
        count += 13
    elif hundreds == 7:
        #seven hundreds and
        count += 15
    elif hundreds == 8:
        #eight hundreds and
        count += 15
    elif hundreds == 9:
        #nine hundreds and
        count += 14
    if tenths == 0 and units == 0:
        #removing 'and'
        count -= 3
    if tenths == 9:
        #ninety
        count += 6
    elif tenths == 8:
        #eighty
        count += 6
    elif tenths == 7:
        #seventy
        count += 7
    elif tenths == 6:
        #sixty
        count += 5
    elif tenths == 5:
        #fifty
        count += 5
    elif tenths == 4:
        #forty
        count += 5
    elif tenths == 3:
        #thirty
        count += 6
    elif tenths == 2:
        #twenty
        count += 6
    if tenths == 1:
        if units == 0:
            count += 3
        elif units == 1:
            count += 6
        elif units == 2:
            count += 6
        elif units == 3:
            count += 8
        elif units == 4:
            count += 8
        elif units == 5:
            count += 7
        elif units == 6:
            count += 7
        elif units == 7:
            count += 9
        elif units == 8:
            count += 8
        elif units == 9:
            count += 8
    else:
        if units == 1:
            count += 3
        elif units == 2:
            count += 3
        elif units == 3:
            count += 5
        elif units == 4:
            count += 4
        elif units == 5:
            count += 4
        elif units == 6:
            count += 3
        elif units == 7:
            count += 5
        elif units == 8:
            count += 5
        elif units == 9:
            count += 4
    return count


answer = 0
for i in range(1, 1001):
    print(str(i) + ' ' + str(letterscounting(i)))
    answer += letterscounting(i)

print(answer)