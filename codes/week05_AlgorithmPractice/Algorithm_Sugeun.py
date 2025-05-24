"""
프로그래머스 / 가장 먼 노드(https://school.programmers.co.kr/learn/courses/30/lessons/49189)
문제를 고른 이유 : 아직 bfs와 dfs 대한 개념이 부족하다고 느껴서 복습하기 위해

문제 설명 : 
노드 n개와 그래프 edge를 입력 받는다. 
시작 노드 1번에서 가장 멀리 떨어져 있는 노드들의 수를 return

문제 풀이 방법 : 
최단경로로 최대거리를 찾는 문제이므로 bfs를 사용, 각 노드까지의 거리를 리스트에 저장
리스트에서 최대값과 빈도수를 찾아 return

defaultdict란 키 값이 없더라도 자동으로 생성하는 특징을 가지고 있다. 
"""

from collections import deque, defaultdict

def solution(n, edge):
    answer = 0

    # 각 노드들 간의 거리 배열 distance 리스트 생성 
    # 1-based 사용 및 직관성을 위해 range(n+1) 및 dist[0]은 사용하지 않는다. 
    dist = [-1 for _ in range(n+1)]
    dist[1] = 0

    # 간선들을 딕셔너리로 정리
    nod_graph = defaultdict(list)
    for u, v in edge:
        nod_graph[u].append(v)
        nod_graph[v].append(u)

    queue = deque([1])

    # BFS 실행
    while queue:
        current = queue.popleft()

        # 인접 노드 탐색
        for node in nod_graph[current]:
            if dist[node] == -1:
                dist[node] = dist[current] + 1   # dist[current] = 시작과 현재 노드간의 거리
                queue.append(node)

    #최대값을 구하고 빈도수 저장
    max_num = max(dist)
    answer = dist.count(max_num)

    return answer
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(6, edge))
