def solution(area):

    if 1 <= area <= 1000000:
        square_areas = []
        while area > 0:
            # Find the largest possible side length of a square
            square_side = int(area ** 0.5)
            # Calculate the area of the square and append it to the list
            square_areas.append(square_side ** 2)
            # Subtract the area of the square from the total area
            area -= pow(square_side, 2)
        return square_areas
