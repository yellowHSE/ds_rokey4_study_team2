# 홍송은
"""
<BFS (Breadth-First Search) - 너비 우선 탐색>
- 그래프나 2차원 배열에서 최단 경로를 찾는 데 자주 사용됨
- 시작 노드에서 가까운 노드부터 먼저 탐색
- 큐(Queue)를 사용하여 탐색할 좌표를 순서대로 저장하고 꺼냄 - FIFO 구조
- 한 칸씩 거리를 늘려가며 탐색하기 때문에 최단 거리 보장

<BFS를 사용하는 이유>
- DFS는 모든 경로를 탐색해야 하므로 비효율적
- BFS는 가까운 칸부터 탐색 → 처음 도착한 경로가 최단 거리

<풀이 흐름>
n x m -> n-1, m-1
1. 시작 좌표 (0,0)를 큐에 넣고 BFS 시작
2. 큐에서 좌표를 꺼내고, 상하좌우로 이동 가능한 칸 확인
3. 이동 가능한 칸이면 (1이고 방문하지 않은 곳):
   - maps[nx][ny] = maps[x][y] + 1 로 거리 갱신
   - 큐에 해당 위치 추가
4. BFS 종료 후, 도착지 maps[n-1][m-1] 값이 변했는지 확인
   - 값이 그대로면 도달 불가 → -1 반환
   - 값이 갱신되어 있으면 그 값이 최단 거리
"""

from collections import deque

def solution(maps):
    n = len(maps)        # 행의 개수
    m = len(maps[0])     # 열의 개수

    # 이동 방향: 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 큐 초기화 (BFS 시작점)
    queue = deque()
    queue.append((0, 0))  # 시작 좌표

    # BFS 수행
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵을 벗어나는 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽이거나 이미 방문한 경우
            if maps[nx][ny] == 0 or maps[nx][ny] > 1:
                continue

            # 이동 가능한 경우: 이전 거리 + 1 저장
            maps[nx][ny] = maps[x][y] + 1
            queue.append((nx, ny))

    # 도착 지점에 도달하지 못한 경우
    if maps[n-1][m-1] == 1:
        return -1

    # 도착 지점에 저장된 값이 최단 거리
    return maps[n-1][m-1]


maps1 = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(maps1))

maps2 = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
print(solution(maps2))