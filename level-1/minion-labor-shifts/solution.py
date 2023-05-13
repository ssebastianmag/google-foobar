def solution(data, n):
    # Check if the length of the data is less than 100 and n is an integer
    if len(data) < 100 and isinstance(n, int):
        # Create a set of distinct elements in the data list
        distinct_set = set(data)

        # Iterate over each unique element in the set
        for id_number in distinct_set:
            if data.count(id_number) >= n + 1:
                # Remove all occurrences of the element from the data list
                data = list(filter(lambda i: i != id_number, data))

        return data
