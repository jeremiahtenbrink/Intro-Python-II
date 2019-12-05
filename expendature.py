import math


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    isEven = d % 2 == 0
    numberOfNotices = 0
    sub = expenditure[:d]
    sub.sort()
    for i in range(d, len(expenditure)):
        if i != d:
            sub = insert(sub, expenditure[i - 1], expenditure[i - d -1])
        if isEven:
            firstNum = sub[math.floor((d / 2) - 1)]
            secondNum = sub[math.ceil((d / 2))]
            median = (firstNum + secondNum) / 2
        else:
            median = sub[math.floor(d / 2)]

        if expenditure[i] >= 2 * median:
            numberOfNotices += 1

    return numberOfNotices



def insert(data, i, d):
    remove_index = bisect.bisect_left(data, expenditure[i - d])
    adding = expenditure[i]
    del data[remove_index]
    bisect.insort(data, adding)
    return data

def find(list, n):
    # Searching for the position
    i = False
    middle = len(list) // 2
    start = 0
    end = len(list) - 1

    while middle < end and middle > start:

        number = list[middle]
        if number == n:
            i = middle
            break
        elif number < n:
            start = middle + 1
            middle = (start + end) // 2
        else:
            end = middle - 1
            middle = (start + end) // 2

    if i == False:
        i = middle
    return i




f = open('./testcase.txt', 'r')
content = f.read()
array = content.split()
for i in range(len(array)):
    array[i] = int(array[i])
print(activityNotifications(array, 10000))
