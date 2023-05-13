def solution(entrances, exits, path):
    num_rooms = len(path)
    num_corridors = len(path[0])

    # Add supersource and supersink to handle multiple entrances and exits
    supersource = num_rooms
    supersink = num_rooms + 1

    # Update the number of rooms and corridors
    num_rooms += 2
    num_corridors += 2

    # Initialize the flow network
    flow_network = [[0] * num_corridors for _ in range(num_rooms)]
    for i in range(num_rooms - 2):
        for j in range(num_corridors - 2):
            flow_network[i][j] = path[i][j]

    # Connect entrances to supersource
    for entrance in entrances:
        # flow_network[supersource][entrance] = float('inf')
        # or
        flow_network[supersource][entrance] = 999999999  # A large enough integer

    # Connect exits to supersink
    for ext in exits:
        # flow_network[exit][supersink] = float('inf')
        # or
        flow_network[ext][supersink] = 999999999  # A large enough integer

    # Ford-Fulkerson algorithm
    def dfs(node, min_capacity, visit):
        visit[node] = True
        if node == supersink:
            return min_capacity
        for k in range(num_rooms):
            if not visit[k] and flow_network[node][k] > 0:
                new_capacity = min(min_capacity, flow_network[node][k])
                result = dfs(k, new_capacity, visit)
                if result > 0:
                    flow_network[node][k] -= result
                    flow_network[k][node] += result
                    return result
        return 0

    max_flow = 0
    while True:
        visited = [False] * num_rooms
        path_capacity = dfs(supersource, float('inf'), visited)
        if path_capacity == 0:
            break
        max_flow += path_capacity

    return max_flow
