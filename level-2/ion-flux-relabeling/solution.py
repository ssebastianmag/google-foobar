def solution(h, q):
    # Check if the height (h) and the length of q are within the allowed ranges,
    # and if the values in q are unique
    if 1 <= h <= 30 and 1 <= len(q) <= 10000 and len(q) == len(set(q)):
        p = []  # Initialize an empty list to store the parents

        for i in range(len(q)):
            if q[i] == (pow(2, h) - 1):  # Check if the node is the root
                p.append(-1)  # Append -1 to indicate no parent
            else:
                current_level = h - 1  # Start from the level below the root

                while current_level > 0:
                    parent = (pow(2, h) - 1)  # Start at the root node
                    left_child = (parent - pow(2, current_level))
                    right_child = parent - 1

                    while True:
                        if q[i] == left_child or q[i] == right_child:
                            p.append(parent)  # Append the parent node
                            current_level = 0  # Stop the loop
                            break
                        else:
                            # Choose the next parent node on the left or right
                            parent = left_child if q[i] < left_child else right_child

                        current_level -= 1
                        left_child = (parent - pow(2, current_level))
                        right_child = parent - 1

        return p  # Return the list of parents
