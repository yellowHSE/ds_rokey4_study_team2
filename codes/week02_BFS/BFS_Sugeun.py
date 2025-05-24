from collections import deque

def solution(maps):
    start = (0, 0)                                                                          #시작 좌표
    end = (4, 4)                                                                            #목표 좌표
    n, m = len(maps), len(maps[0])                                                          #maps의 길이를 n, m에 저장
    queue = deque([(start[0], start[1], 0)])                                                #데크(x, y, 이동거리)
    visited = [[False] * m for _ in range(n)]                                               #False로 이루어진 5x5 이차원 배열 생성
    visited[start[0]][start[1]] = True                                                      #시작 위치를 True
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]                                          #상하좌우 이동 리스트 생성
    while queue:
        x, y, dist = queue.popleft()                                                        #큐 값을 x, y, dist 에 저장(맨 처음은 0, 0, 0)
        if (x, y) == end:
            return dist + 1                                                                 #x, y가 목표값일 경우, 이동거리 + 1을 리턴(맨 처음 본인을 탐색안했기 때문)
        for dx, dy in direction:
            nx, ny = x + dx, y + dy                                                         #x, y가 목표값이 아닐 경우, x, y에 상하좌우 이동 명령 > nx, ny에 좌표 저장
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:   #nx, ny가 5x5 리스트를 나가지 않고, 1이면서 아직 방문하지 않았다면
                queue.append((nx, ny, dist + 1))                                            #큐에 현재 좌표 nx, ny 와 이동거리에 +1 삽입
                visited[nx][ny] = True                                                      #False 였던 자리를 True 로 변환
    return -1                                                                               #목표에 도착하지 못했다면 -1 리턴

