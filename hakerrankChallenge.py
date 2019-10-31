def numofPrizes(k, marks):
    length = len(marks)
    i = 0

    while i < length:
        if marks[i] == 0:
            marks.remove(marks[i])
            length = length - 1
            continue
        i = i + 1

    print(marks)
    marks.sort(reverse = True)
    number = k
    if number > len(marks):
        number = len(marks)

    if number == 0:
        return 0

    lowest = marks[number - 1]

    sub = marks[number:]

    for i in range(len(sub)):
        if marks[k + i] == lowest:
            number += 1
        else:
            break
    return number


print(numofPrizes(4, [0, 0, 0, 60, 80, 100]))
