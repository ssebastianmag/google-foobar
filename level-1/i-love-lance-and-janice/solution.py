def solution(x):
    decoded_msg = ''
    for y in range(len(x)):
        char = x[y]

        # for each lowercase character, get its reversed position
        # in unicode code points and append the resultant character
        if 'a' <= char <= 'z':
            decoded_msg += chr(ord('a') + 25 - (ord(char) - ord('a')))
        else:
            decoded_msg += char

    return decoded_msg


print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
# output: did you see last night's episode?

print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
# output: Yeah! I can't believe Lance lost his job at the colony!!
