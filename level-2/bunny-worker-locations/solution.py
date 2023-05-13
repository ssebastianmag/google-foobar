def solution(x, y):
    worker_id = 1  # Initialize worker ID as 1
    diagonal_index = x + y - 1  # Calculate the diagonal index

    # Calculate the worker ID by summing the numbers in the diagonal
    for i in range(1, diagonal_index):
        worker_id += i

    # Adjust the worker ID based on the x-coordinate
    worker_id += x - 1
    return str(worker_id)  # Return the worker ID as a string
