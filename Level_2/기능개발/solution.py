def solution(progresses, speeds):
    answer = []
    # 각 배포마다 몇개의 기능이 배포되는지
    counts = [0 for i in range(len(progresses))]
    
    for i in range(len(progresses)):
        count = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            count += 1
        counts[i] = count
    
    print(counts)
    while counts:
        start = counts.pop(0)
        temp = [start]
        
        while counts:
            if counts[0] <= start:
                temp.append(counts.pop(0))
            else:
                break
        
        answer.append(len(temp))
        
        print(f'start : {start} temp: {temp}')
    return answer