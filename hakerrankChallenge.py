def numofPrizes(k, marks):
    # Keep a histogram of all the student scores
    count = [0] * 101

    for m in marks:
        count[m] += 1

    # Count of all ranking students
    ranking_student_count = 0

    # Go down the histogram from 100 to 1
    # (Students who score 0 are ineligible)
    for i in range(100, 0, -1):
        people_with_score = count[i]

        # If some people got this score
        if people_with_score != 0:

            # Add them to the total count
            ranking_student_count += people_with_score

            # And that many fewer ranks are now available
            k -= people_with_score

            # If no ranks left, we're done
            if k <= 0:
                break

    return ranking_student_count


print(numofPrizes(4, [0, 60, 60, 60, 80, 100]))
