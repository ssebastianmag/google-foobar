def solution(xs):
    if len(xs) == 1:  # Output: unique value when there's only one element in the list
        return str(xs[0])

    # Separate the list into positive and negative values
    positives = [x for x in xs if x > 0]
    negatives = [x for x in xs if x < 0]

    # If the number of negative items is odd, remove the highest value
    if len(negatives) % 2 != 0:
        negatives.remove(max(negatives))

    # If both lists are empty, output: 0
    if len(negatives) == 0 and len(positives) == 0:
        return str(0)

    # Calculate the product of the positive and negative values
    max_product = 1
    for x in positives + negatives:
        max_product *= x

    return str(max_product)
