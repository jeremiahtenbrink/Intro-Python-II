from collections import defaultdict


def numofPrizes(marks, k):
    marks.sort(reverse = True)
    number = k
    if number > len(marks):
        number = len(marks)

    lowest = marks[number - 1]

    sub = marks[number:]

    for i in range(len(sub)):
        if marks[k + i] == lowest:
            number += 1
        else:
            break

    return number


print(numofPrizes([20,40, 40, 60, 80, 100], 4))
