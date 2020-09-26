def dfs(computers, visited, i):
    if visited[i] == 0:
        visited[i] = 1
    for j in range(len(computers)):
        if computers[i][j] == 1 and visited[j] == 0:
            dfs(computers, visited, j)

def solution(n, computers):
    # dfs 는 방문한 곳을 기억해야한다!
    visited = [0]*n
    answer = 0
    while 0 in visited:
        # 방문한 하지 않은 곳이 없을 때까지
        for i in range(n):
            if visited[i] == 0:
                # 만약 i 번째를 방문하지 않았다면,
                dfs(computers, visited, i)
                answer += 1
                # 왜 answer + 1 하는가?
                # dfs 함수를 보면, 방문하지 하지 않은 곳 중 연결된 곳이 있으면 
                # 계속 타고 들어간다.
                # 연결이 다 된것이 하나로 쳐지고, 
                # 만약 연결이 안된거면 그것 또한 하나의 네트워크이다.
    return answer