def solution(s, n):
    answer = []

    for char in s:
        if char == ' ':
            answer.append(' ')
        else:
            if ord(char) >= 65 and ord(char) <= 90:
                #대문자
                new = ord(char) + n
                if new > 90:
                    new -= 26
                answer.append(chr(new))
            elif ord(char) >= 97 and ord(char) <= 122:
                #소문자
                new = ord(char) + n
                if new > 122:
                    new -= 26
                answer.append(chr(new))
            
    return ''.join(answer)