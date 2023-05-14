def solution(n, b):
    zlist = []  # List to store encountered values
    k = len(n)  # Length of the minion ID

    if int(n) > 0 and 2 <= k <= 9 and 2 <= b <= 10:
        while True:
            ln = list(n)
            x = ''.join(sorted(ln, reverse=True))  # Generate x by sorting digits of n in descending order
            y = ''.join(sorted(ln))  # Generate y by sorting digits of n in ascending order
            z = int(x, b) - int(y, b)

            base_b_z = []
            while z != 0:
                base_b_z.insert(0, str(z % b))  # Convert z to base b
                z = z // b
            z = ''.join(base_b_z)

            if len(z) < k:
                z = z.zfill(k)  # Add leading zeros to z if necessary

            if z in zlist:
                return len(zlist) - zlist.index(z)  # Found a cycle, return the length of the cycle
            elif z not in zlist:
                zlist.append(z)  # Add z to the list of encountered values
                n = z  # Update n for the next iteration
