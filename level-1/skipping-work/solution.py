def solution(x, y):
    # Convert the lists into sets for efficient comparison
    set_x = set(x)
    set_y = set(y)

    # Find the additional ID by subtracting sets and returning the popped element
    additional_id = (set_x - set_y).pop() if len(set_x) > len(set_y) else (set_y - set_x).pop()
    return additional_id
