def solution(m, f):
    m = int(m)
    f = int(f)
    generations = 0

    # Check if the input values are within the valid range
    if 1 <= m <= pow(10, 50) >= f >= 1:

        # Check for impossible scenarios
        if (m % 2 == 0 and f % 2 == 0) or m < 1 or f < 1:
            return 'impossible'

        # Perform the replication process until reaching the desired number of bombs
        while m != 1 and f != 1:

            # Check for impossible scenarios
            if m % f == 0 or f % m == 0:
                return 'impossible'
            elif m > f:
                # Replicate Mach bombs from Facula bombs
                generations += int(m / f)
                m = m % f
                m, f = f, m
            else:
                # Replicate Facula bombs from Mach bombs
                generations += int(f / m)
                f = f % m
                f, m = m, f

        # Add remaining bombs to reach the desired number
        if m > f:
            generations += m - 1
        else:
            generations += f - 1

        return str(generations)
