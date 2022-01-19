def solution(data, n):
    if len(data) < 100 and isinstance(n, int):
        distinct_set = set(data)
        for id_number in distinct_set:
            if data.count(id_number) >= n + 1:
                data = list(filter(lambda i: i != id_number, data))

        return data


print(solution([1, 2, 3], 0))
# output: []

print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
# output: [1, 4]
