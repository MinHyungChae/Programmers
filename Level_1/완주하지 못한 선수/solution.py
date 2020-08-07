import collections

def solution(participant, completion):
    # 각각의 이름과 갯수에 대한 dictionary 를 만들고, completion 의 길이는 participant 의 길이보다 1 작으므로 무조건 한명의 완주하지 못한 선수가 나온다. 따라서 둘을 빼면 답을 구할 수 있다.
    
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    return list(answer.keys())[0]