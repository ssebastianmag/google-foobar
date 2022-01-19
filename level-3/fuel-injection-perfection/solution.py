def solution(n):

    pellets = int(n)
    num_of_operations = 0
    while pellets != 1:

        if (pellets % 2) == 0:
            pellets /= 2
            num_of_operations += 1
        else:
            if (pellets + 1)/2 == 1:
                pellets += 1
                num_of_operations += 1

            elif (pellets - 1)/2 == 1:
                pellets -= 1
                num_of_operations += 1

            elif ((pellets + 1)/2 % 2) == 0:
                pellets += 1
                num_of_operations += 1

            elif ((pellets - 1)/2 % 2) == 0:
                pellets -= 1
                num_of_operations += 1

    return num_of_operations


print(solution('15'))
# output: 5

print(solution('4'))
# output: 2
