def solution(m, f):

    m = int(m)
    f = int(f)
    generations = 0

    if 1 <= m <= pow(10, 50) >= f >= 1:

        if (m % 2 == 0 and f % 2 == 0) or m < 1 or f < 1:
            return 'impossible'

        while m != 1 and f != 1:

            if m % f == 0 or f % m == 0:
                return 'impossible'
            elif m > f:
                generations += int(m / f)
                m = m % f
                m, f = f, m
            else:
                generations += int(f / m)
                f = f % m
                f, m = m, f

        if m > f:
            generations += m - 1
        else:
            generations += f - 1

        return str(generations)


print(solution('4', '7'))
# output: 4

print(solution('2', '1'))
# output: 1

print(solution('2', '2'))
# output: 'impossible'

print(solution('1', '1'))
# output: 0
