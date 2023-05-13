def gcd(a, b):
    # Euclidean algorithm to calculate the greatest common divisor of a and b
    while b:
        a, b = b, a % b
    return a


def solution(s):
    n = len(s)
    for i in range(1, n + 1):
        if n % i == 0:
            valid = True
            # Check if each segment of length i contains the same characters
            for j in range(i):
                for k in range(j, n, i):
                    if s[k] != s[j]:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                # Return the number of equal parts if a valid divisor is found
                return n // i
    # If no valid divisor is found, return 1 indicating the entire cake cannot be divided into equal parts
    return 1
