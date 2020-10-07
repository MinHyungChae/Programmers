# 정확성 46.7

def solution(m, musicinfos):
    answer = list()
    
    for music in musicinfos:
        info_list = music.split(',')
        duration = (int(info_list[1][:2]) - int(info_list[0][:2]))*60 + int(info_list[1][3:]) - int(info_list[0][3:])
        
        title = info_list[2]
        lyric = info_list[3]
        
        total_lyric = lyric*(duration//len(lyric)) + lyric[:duration%(len(lyric))]
        
        if m in total_lyric:
            check_m = m+'#'
            if check_m in total_lyric:
                if total_lyric.index(m) != total_lyric.index(check_m):
                    answer.append([title, duration, info_list[0]])
            else:    
                answer.append([title, duration, info_list[0]])
    
    
    if len(answer) == 1:
        return answer[0][0]
    elif len(answer) == 0:
        return "(None)"
    else:
        answer = sorted(answer, key = lambda x: (-x[1], x[2]))
        return answer