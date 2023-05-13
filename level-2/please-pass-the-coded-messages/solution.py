from itertools import combinations


def solution(l):

    l.sort(reverse=True)  # Sort the input list in descending order

    # Iterate over different lengths of combinations in descending order
    for x in range(len(l), 0, -1):
        # Generate combinations of the elements in the list
        for c in combinations(l, x):
            # Join all digits in the combination to form a resulting number
            largest_number = ''.join([str(x) for x in c])

            # Check if the resulting number is divisible by 3
            if int(largest_number) % 3 == 0:
                return largest_number

    return 0
