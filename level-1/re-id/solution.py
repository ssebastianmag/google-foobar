def solution(start_index):
    # Return a slice of five prime numbers starting from the given index
    return primes[start_index:start_index + 5]


primes = ''  # Initialize an empty string to store prime numbers
for i in range(2, 21000):
    if len(primes) < 10000:
        # Check if the current number is prime
        if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
            primes += str(i)  # Add the prime number to the primes string
    else:
        break  # Stop generating prime numbers if we have 10000 of them
