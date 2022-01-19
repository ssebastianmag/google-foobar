def solution(h, q):

    if 1 <= h <= 30 and 1 <= len(q) <= 10000 and len(q) == len(set(q)):
        p = []

        for i in range(len(q)):
            if q[i] == (pow(2, h) - 1):  # root node won't have a converter on top
                p.append(-1)

            else:
                current_level = h - 1
                while current_level > 0:
                    parent = (pow(2, h) - 1)  # starts at root node
                    left_child = (parent - pow(2, current_level))
                    right_child = parent - 1

                    while True:

                        if q[i] == left_child or q[i] == right_child:
                            p.append(parent)
                            current_level = 0
                            break
                        else:
                            # next parent node at left or right
                            parent = left_child if q[i] < left_child else right_child

                        current_level -= 1
                        left_child = (parent - pow(2, current_level))
                        right_child = parent - 1
        return p


print(solution(3, [7, 3, 5, 1]))
# output: -1,7,6,3

print(solution(5, [19, 14, 28]))
# output: 21,15,29
