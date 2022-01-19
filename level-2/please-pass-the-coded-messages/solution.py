from itertools import combinations


def solution(l):

    # get all different combinations in descending order
    l.sort(reverse=True)
    for x in range(len(l), 0, -1):
        for c in combinations(l, x):

            # join all digits into a resulting number
            largest_number = ''.join([str(x) for x in c])

            # check if this number can be divided by 3
            if int(largest_number) % 3 == 0:
                return largest_number
    return 0


print(solution([3, 1, 4, 1]))
# output: 4311

print(solution([3, 1, 4, 1, 5, 9]))
# output: 94311
