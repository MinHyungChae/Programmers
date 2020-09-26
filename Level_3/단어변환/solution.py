def dfs(begin, target, words, answer):
    if begin == target:
        return answer
    diff = []
    for i in range(len(words)):
        diffCnt = 0
        for j in range(len(begin)):
            if words[i][j] != begin[j]:
                diffCnt += 1
        if diffCnt == 1 and words[i] == target:
            answer.append(diffCnt)
            return answer
        diff.append(diffCnt)
    if not 1 in diff:
        return 0
    else:
        next = words[diff.index(1)]
        answer.append(next)
        words.pop(diff.index(1))
        dfs(next, target, words, answer)

def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        answer = []
        dfs(begin, target, words, answer)
    return len(answer)