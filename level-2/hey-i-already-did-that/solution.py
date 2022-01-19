def solution(n, b):
    
    zlist = []
    k = len(n)

    if int(n) > 0 and 2 <= k <= 9 and 2 <= b <= 10:
        while True:
            ln = list(n)
            x = ''.join(sorted(ln, reverse=True))
            y = ''.join(sorted(ln))
            z = int(x, b) - int(y, b)

            base_b_z = []
            while z != 0:
                base_b_z.insert(0, str(z % b))
                z = z // b
            z = ''.join(base_b_z)

            if len(z) < k:
                z = z.zfill(k)

            if z in zlist:
                return len(zlist) - zlist.index(z)

            elif z not in zlist:
                zlist.append(z)
                n = z


print(solution('1211', 10))
# output: 1

print(solution('210022', 3))
# output: 3
