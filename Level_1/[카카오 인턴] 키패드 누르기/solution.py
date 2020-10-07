def find_idx(key, keypad):
    for i in range(len(keypad)):
        for j in range(3):
            if keypad[i][j] == key:
                return [i, j]

def solution(numbers, hand):
    answer = []
    left_now = '*'
    right_now = '#'
    
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
        
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer.append('L')
            left_now = num
        elif num == 3 or num == 6 or num == 9:
            answer.append('R')
            right_now = num
        else:
            num_idx = find_idx(num, keypad)
            left_idx = find_idx(left_now, keypad)
            right_idx = find_idx(right_now, keypad)
            
            left_dist = abs(left_idx[0]-num_idx[0]) + abs(left_idx[1] - num_idx[1])
            right_dist = abs(right_idx[0]-num_idx[0]) + abs(right_idx[1] - num_idx[1])
    
            if left_dist < right_dist:
                answer.append('L')
                left_now = num
            elif right_dist < left_dist:
                answer.append('R')
                right_now = num
            elif left_dist == right_dist:
                if hand == 'left':
                    answer.append('L')
                    left_now = num
                elif hand == 'right':
                    answer.append('R')
                    right_now = num
                
    
    return ''.join(answer)