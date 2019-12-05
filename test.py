from collections import defaultdict
import math

def arrayManipulation(expenditure, d):
    isEven = d % 2 == 0
    numberOfNotices = 0
    sub = expenditure[:d]
    sub.sort()
    for i in range(d, len(expenditure)):
        if i != d:
            sub.remove(expenditure[i - d])
            sub = insert(sub, expenditure[i -1])
        if isEven:
            firstNum = sub[math.floor((d/2) -1)]
            secondNum = sub[math.ceil((d/2))]
            median = (firstNum + secondNum)/2
        else:
            median = sub[math.floor(d/2)]

        if expenditure[i] >= 2 * median:
            numberOfNotices += 1

    return numberOfNotices


def insert(list, n):
    # Searching for the position
    for i in range(len(list)):
        if list[i] > n:
            index = i
            break

    # Inserting n in the list
    list = list[:i] + [n] + list[i:]
    return list


print(arrayManipulation([1, 2, 3, 4, 4], 4))
