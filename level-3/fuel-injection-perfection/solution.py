def solution(n):
    pellets = int(n)
    num_of_operations = 0

    # Perform operations until there is only 1 pellet remaining
    while pellets != 1:

        # Check if the number of pellets is even
        if (pellets % 2) == 0:
            pellets /= 2
            num_of_operations += 1
        else:
            # Increment pellets by 1
            if (pellets + 1)/2 == 1:
                pellets += 1
                num_of_operations += 1

            # Decrement pellets by 1
            elif (pellets - 1)/2 == 1:
                pellets -= 1
                num_of_operations += 1

            # Increment pellets by 1
            elif ((pellets + 1)/2 % 2) == 0:
                pellets += 1
                num_of_operations += 1

            # Decrement pellets by 1
            elif ((pellets - 1)/2 % 2) == 0:
                pellets -= 1
                num_of_operations += 1

    return num_of_operations
