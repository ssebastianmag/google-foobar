def solution(s):

    salutes = 0  # Iterate through each character in the hallway string
    for i in range(len(s)):
        if s[i] == '>':
            # If an employee is walking to the right (>)...
            # Check for employees walking to the left (<<) ahead and count salutes
            salutes += s[i+1:].count('<')
        elif s[i] == '<':
            # If an employee is walking to the left (<)...
            # Check for employees walking to the right (>>) behind and count salutes
            salutes += s[:i].count('>')

    return salutes
