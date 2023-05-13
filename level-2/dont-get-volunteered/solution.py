class Position:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__moves_from_source = 0

    def set_moves_from_source(self, moves):
        self.__moves_from_source = moves

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_moves_from_source(self):
        return self.__moves_from_source


def solution(src, dest):
    # Check if the source and destination are within the valid range
    if 0 <= src <= 63 >= dest >= 0:
        src_x, src_y = int(src / 8), int(src % 8)
        visited_positions = []  # Keep track of visited positions
        points = [Position(src_x, src_y)]  # Initialize the starting position

        while len(points) > 0:
            position = points.pop(0)  # Get the next position from the list

            if (position.get_x(), position.get_y()) == (int(dest / 8), int(dest % 8)):
                return position.get_moves_from_source()  # Return the number of moves from the source

            if position not in visited_positions:
                visited_positions.append(position)  # Mark the position as visited

                # Generate potential new positions
                for p in [(-2, 1), (-2, -1), (1, 2), (-1, 2), (2, 1), (2, -1), (-1, -2), (1, -2)]:
                    x, y = position.get_x() + p[0], position.get_y() + p[1]

                    if 0 <= x < 8 > y >= 0:
                        new_point = Position(x, y)  # Create a new position
                        new_point.set_moves_from_source(position.get_moves_from_source() + 1)  # Update moves count
                        points.append(new_point)  # Add the new position to the list of points to explore


print(solution(0, 1))
# output: 3

print(solution(19, 36))
# output: 1
