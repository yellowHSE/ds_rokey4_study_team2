from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    # 그래프 구성
    for start, end in tickets:
        graph[start].append(end)

    # 알파벳 순으로 정렬
    for airport in graph:
        graph[airport].sort(reverse=True)

    route = []

    print(graph)

    def dfs(current):
        while graph[current]:
            next_airport = graph[current].pop()
            dfs(next_airport)
        route.append(current)

    dfs("ICN")

    result = route[::-1]
    print(result)
    return result
W
# 예시 실행

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
