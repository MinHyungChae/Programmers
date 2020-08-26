# 다른 사람 제출 코드 참고
# 점수 : 100 / 100

from operator import itemgetter

def solution(genres, plays):
    answer = []
    g_dict = {}

    # make dict with genre, play, index
    for i in range(0, len(genres)) :
        if genres[i] not in g_dict :
            g_dict[genres[i]] = []
            g_dict[genres[i]].append(0);
        g_dict[genres[i]].append( (i, plays[i]) )
        g_dict[genres[i]][0] += plays[i]

    # sort sum of play descending order.
    a = list(g_dict.values())
    a.sort(key=itemgetter(0), reverse=True)

    # pop the most played genre.
    # and selecte the most played two songs.
    while a :
        max = -1
        # remove total sum of the genre played.
        a[0].pop(0)

        # sort by number played on increasing order.
        a[0].sort(key=itemgetter(1), reverse=True) 

        # extract top 2 songs and append to answer.
        for i in range(0, len(a[0])) :
            if (i >= 2) :
                break
            answer.append(a[0][i][0])

        # remove current genre from list.
        a.pop(0)

    return answer