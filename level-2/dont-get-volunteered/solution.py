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

    if 0 <= src <= 63 >= dest >= 0:

        src_x, src_y = int(src / 8), int(src % 8)
        visited_positions = []
        points = [Position(src_x, src_y)]

        while len(points) > 0:
            position = points.pop(0)

            if (position.get_x(), position.get_y()) == (int(dest / 8), int(dest % 8)):
                return position.get_moves_from_source()

            if position not in visited_positions:
                visited_positions.append(position)

                for p in [(-2, 1), (-2, -1), (1, 2), (-1, 2), (2, 1), (2, -1), (-1, -2), (1, -2)]:
                    x, y = position.get_x() + p[0], position.get_y() + p[1]

                    if 0 <= x < 8 > y >= 0:
                        new_point = Position(x, y)
                        new_point.set_moves_from_source(position.get_moves_from_source() + 1)
                        points.append(new_point)


print(solution(0, 1))
# output: 3

print(solution(19, 36))
# output: 1
