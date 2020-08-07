def solution(board, moves):
    bucket = list()
    count = 0
    moves = [move -1 for move in moves] # index 형태로 변환
    
    def boom():
        if (len(bucket) >= 2):
            if (bucket[len(bucket)-2] == bucket[len(bucket)-1]):
                bucket.pop()
                bucket.pop()
                return 2
            else:
                return 0
        else:
            return 0
    
    for move in moves :
        for i in range(0, len(board)) :
            if (board[i][move] != 0) :
                bucket.append(board[i][move])
                board[i][move] = 0
                count += boom()
                break
            else :
                if (i < len(board)-1) :
                    continue
                else :
                    break
    
    return count