def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    else:
        d = sorted(d)
        d_sum = 0
        answer = []
        for di in d:
            d_sum += di
            if d_sum <= budget:
                answer.append(di)
            else:
                break
        return len(answer)
            