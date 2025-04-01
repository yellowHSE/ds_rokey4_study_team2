# n개의 컴퓨터에 대해 배열 computers 를 입력받고 연결되어있는 네트워크의 개수 출력
# 가장 깊이 탐색하여 연결된 모든 컴퓨터를 찾는다.
# 한번 끊긴다면 네트워크가 분리 된것
# False로 이루어진 배열을 방문하여 True 로 바꾸는 과정


def solution(n, computers):
    answer = 0                                                              # 답변
    visited = [False for _ in range(n)]                                     # [False] 리스트 생성

    for com in range(n):
        if visited[com] == False:                                           # 네트워크가 연결되지 않았다면
            DFS(n, computers, com, visited)                                 # 재귀함수 시작
            answer += 1                                                     # 네트워크 개수
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True                                                     # 연결되지 않은 컴퓨터에 대해 True 변환

    for node in range(n):                                                   # 대각선 x, False 일때 요소값이 1인 컴퓨터의 인덱스
        if node != com and visited[node] == False and computers[node][com] == 1:     
            DFS(n, computers, node, visited)

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))
