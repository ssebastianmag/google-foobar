def solution(x):
    decoded_msg = ''
    for y in range(len(x)):
        char = x[y]
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # For each lowercase character, calculate its reversed position
            # in the alphabet by subtracting its ASCII value from 'a' and
            # adding the difference from 'z', and append the resultant character
            decoded_msg += chr(ord('a') + 25 - (ord(char) - ord('a')))
        else:
            # If the character is not a lowercase letter, leave it unchanged
            decoded_msg += char
    return decoded_msg
