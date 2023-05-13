def calc_post_column(current, previous, size):
    """
    Calculate the gas distribution in the next column based on the current column and the previous column.

    Args:
        current (int): Current column's gas distribution represented as a binary number.
        previous (int): Previous column's gas distribution represented as a binary number.
        size (int): Number of rows in the grid.

    Returns:
        int: Gas distribution in the next column represented as a binary number.
    """
    result = 0
    for idx in range(size):
        bit1 = (current & (1 << idx)) >> idx
        bit2 = (current & (1 << (idx + 1))) >> (idx + 1)
        bit3 = (previous & (1 << idx)) >> idx
        bit4 = (previous & (1 << (idx + 1))) >> (idx + 1)
        _sum = bit1 + bit2 + bit3 + bit4
        if _sum == 1:
            result |= 1 << idx
    return result


def solution(g):
    """
    Calculate the number of possible previous states of the gas grid after 1 time step.

    Args:
        g (List[List[bool]]): Current state of the gas grid.

    Returns:
        int: Number of possible previous states.
    """
    height = len(g)
    width = len(g[0])
    possibilities_count = 2 << height
    input_array = []

    for x_idx in range(width):
        value = 0
        for y_idx in range(height):
            if g[y_idx][x_idx]:
                value |= 1 << y_idx
        input_array.append(value)

    # Prepare count_array
    count_array = [1] * possibilities_count

    # Prepare element_to_pre_pair
    element_to_pre_pair = {idx: [] for idx in range(possibilities_count)}

    for idx1 in range(possibilities_count):
        for idx2 in range(possibilities_count):
            l = calc_post_column(idx1, idx2, height)
            element_to_pre_pair[l].append((idx1, idx2))

    # Go through calculations
    for w_idx in range(width):
        new_count = [0] * possibilities_count
        for pre_element in element_to_pre_pair[input_array[w_idx]]:
            new_count[pre_element[0]] += count_array[pre_element[1]]
        count_array = new_count

    # Sum result
    total_sum = sum(count_array)

    return total_sum
