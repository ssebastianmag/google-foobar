def solution(l):
    count = 0
    n = len(l)

    # Create a list to store the count of numbers that divide a particular number
    divisors = [0] * n

    for i in range(n):
        for j in range(i):
            # Check if the current element divides the previous element
            if l[i] % l[j] == 0:
                # Increment the count of divisors for the current element
                divisors[i] += 1
                # Increment the count of lucky triples by the count of divisors of the previous element
                count += divisors[j]
    return count
