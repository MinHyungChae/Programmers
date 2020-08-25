# 정확성 : 84.6
# 효율성 : 15.4
# 합계 : 100.0 / 100.0

# v2 에서 효율성 문제를 개선. 최종 제출 답안
# 이전 i for 문에서 이미 answer = False 인 경우를 찾았음에도 계속 도는 문제를 제거. 첫번째 턴에서 False 케이스 잡았을 때 바로 break 로 탈출하도록 로직 변경.

def solution(phone_book):
    answer = True
    # 문자열의 길이 순으로 배열 정렬
    phone_book.sort(key = len)
    
    for i in range(0, len(phone_book)):
        if answer == True:
            for j in range(i+1, len(phone_book)):
                keyword = str(phone_book[i])
                target = phone_book[j][0:len(keyword)]
                if keyword == target:
                    answer = False
                    break
        else:
            break
    return answer