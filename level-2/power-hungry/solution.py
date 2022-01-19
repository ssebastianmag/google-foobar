def solution(xs):

    if len(xs) == 1:  # output = unique value
        return str(xs[0])

    # get list of positive and negative values
    positives = [x for x in xs if x > 0]
    negatives = [x for x in xs if x < 0]

    # if number of negative items is odd, then remove highest value
    if len(negatives) % 2 != 0:
        negatives.remove(max(negatives))

    # if both lists are empty, output = 0
    if len(negatives) == 0 and len(positives) == 0:
        return str(0)

    # get product of positives and negatives
    max_product = 1
    for x in positives + negatives:
        max_product *= x
    return str(max_product)


print(solution([2, 0, 2, 2, 0]))
# output: 8

print(solution([-1, -3, 4, -5]))
# output: 60
