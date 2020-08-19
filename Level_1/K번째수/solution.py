def solution(array, commands):
    answer = []
    # commands[i][0] = i
    # commands[i][1] = j    
    # commands[i][2] = k
    
    for i in range(0, len(commands)):
        start = commands[i][0]
        end = commands[i][1]
        modified_array = array[start -1 : end]
        modified_array.sort()
        answer.append(modified_array[commands[i][2] -1])
        
    return answer