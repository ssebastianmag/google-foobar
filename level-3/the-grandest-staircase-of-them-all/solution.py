def solution(n):
    # Create a 2D solutions matrix to store the number of staircases for each brick count
    solutions = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(n + 1):
            solutions[i][j] = 0
            max_bricks = (j) * (j + 1) // 2

            # Check conditions to determine the number of staircases
            if i == 0 or j == 0 or i > max_bricks:
                solutions[i][j] = 0
                continue
            if i == j:
                solutions[i][j] = 1
            if max_bricks == i:
                solutions[i][j] = 1
            if i < max_bricks:
                # Calculate the number of staircases using dynamic programming
                for k in range(min(i, j), 0, -1):
                    solutions[i][j] += solutions[i - k][k - 1]
                solutions[i][j] = max(solutions[i][j], solutions[i][j - 1])

    return solutions[n][n] - 1
