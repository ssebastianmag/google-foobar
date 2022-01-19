import math


def solution(dimensions, your_position, guard_position, distance):

    if 1 < dimensions[0] <= 1250 >= dimensions[1] > 1 and 1 < distance <= 10000 and \
           dimensions[0] > your_position[0] > 0 < your_position[1] < dimensions[1] and \
           dimensions[0] > guard_position[0] > 0 < guard_position[1] < dimensions[1]:

        vector_bearings, your_coordinates, guard_coordinates = ([] for _ in range(3))
        map_entities = [(your_coordinates, your_position), (guard_coordinates, guard_position)]
        shot_vector = dict()

        for map_entity in map_entities:
            x, y = ([] for _ in range(2))

            for i in range(len(map_entities)):
                floor = distance//dimensions[i]+2

                for p in range(-floor, floor):
                    point = map_entity[1][i]
                    wall = [2 * point, 2 * (dimensions[i] - point)]
                    step = 1 if p < 0 else -1
                    for j in range(p, 0, step):
                        point -= step * wall[(j + (p < 0)) % 2]

                    if i == 0:
                        x.append(point)
                    else:
                        y.append(point)

            for x_val in x:
                for y_val in y:
                    map_entity[0].append((x_val, y_val))

        for coordinates in [your_coordinates, guard_coordinates]:

            for x, y in coordinates:
                dx, dy = your_position[0] - x, your_position[1] - y
                magnitue = pow((dx*dx + dy*dy), 0.5)
                theta = math.atan2(dx, dy)

                if [x, y] == your_position or distance < magnitue or not \
                    ((theta in shot_vector and shot_vector[theta] > magnitue) or
                        theta not in shot_vector):
                    continue

                shot_vector[theta] = magnitue
                if coordinates == guard_coordinates:
                    vector_bearings.append(theta)

        return len(set(vector_bearings))


print(solution([3, 2], [1, 1], [2, 1], 4))
# output: 7

print(solution([300, 275], [150, 150], [185, 100], 500))
# output: 9
