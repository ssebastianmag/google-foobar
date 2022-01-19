def solution(area):

    if 1 <= area <= 1000000:
        square_areas = []

        while area > 0:
            square_side = int(area ** 0.5)
            square_areas.append(square_side ** 2)
            area -= pow(square_side, 2)

        return square_areas


print(solution(15324))
# output: [15129, 169, 25, 1]

print(solution(12))
# output: [9, 1, 1, 1]
