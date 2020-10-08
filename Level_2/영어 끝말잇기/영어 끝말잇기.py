def solution(n, words):
    answer = []
    turn = 0
    who = 0
    used = []
    for i in range(len(words)):
        
        if i % n == 0:
            turn +=1 
        who = i%n + 1
        
        if i == 0:
            used.append(words[i])
            continue
            
        else:
            if words[i] in used:
                return [who, turn]
            else:
                prev = words[i-1][-1]
                now = words[i][0]
                print(f'{prev}, {now}')
                if prev != now:
                    return [who, turn]
                else:
                    used.append(words[i])

    return [0, 0]