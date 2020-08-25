# 정확성 84.6
# 효율성 0.0
# 합계 84.6 / 100.0

# phone_book 리스트를 길이 순으로 정렬하고
# 첫번째 부터 순차적으로 자신 다음에 있는 요소들에서 자신을 포함한 경우 return False 하고 break 건다
# v1에서 효율성을 제외하고 테스트 케이스에서 오답이 나는 경우가 있어 로직을 수정하였다.
# v1에서는 자기 자신을 '포함' 하면 false 를 반환했는데, 문제를 다시 읽어보니 시작 위치부터 일치해야한다는 것을 알았다. 따라서 이를 수정했더니 효율성을 제외하고는 모든 테스트 케이스를 통과하였다.

def solution(phone_book):
    answer = True
    # 문자열의 길이 순으로 배열 정렬
    phone_book.sort(key = len)
    
    for i in range(0, len(phone_book)):
        for j in range(i+1, len(phone_book)):
            keyword = str(phone_book[i])
            target = phone_book[j][0:len(keyword)]
            if keyword == target:
                answer = False
                break        
    return answer