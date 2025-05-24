# 3주차 - DFS 깊이 우선 탐색
# 프로그래머스 - 타겟 넘버
"""
<문제 요약>
정수 배열 numbers가 주어졌을 때,
각 숫자 앞에 + 또는 -를 붙여 연산 결과가 target이 되는 경우의 수를 구하라.

중요) 숫자의 순서를 바꾸지 않고 계산 = DFS 적합
※ 만약 숫자의 순서를 바꿔도 된다면 → 순열(Permutation)도 함께 사용
   이유: 순서가 달라진 조합을 서로 다른 경우로 인정하므로 경우의 수가 늘어남
        numbers = [1, 2]
        순서 바꾸지X : 총 4가지
        순서 바꾸기O : [1, 2] 조합 + [2, 1] 조합 = 총 8가지

<DFS (Depth-First Search) - 깊이 우선 탐색>
- 그래프나 트리에서 한 방향으로 끝까지 탐색한 후, 다시 돌아와 다른 경로 탐색
- 재귀 or 스택 사용해서 구현
- 모든 조합이나 경우의 수를 탐색해야 하는 문제에 적합
- 백트래킹, 브루트포스, 조합 문제에서 자주 활용

<풀이 흐름>
1. 트리의 루트: 0부터 시작
2. 각 Depth는 numbers의 인덱스를 의미
3. 왼쪽 자식 노드: 해당 숫자 음수(-)로 더하기
4. 오른쪽 자식 노드: 해당 숫자 양수(+)로 더하기
5. 마지막 숫자까지 도달한 후(leaf node까지 도달) 누적된 합이 target과 일치하면 카운트 증가

<예시: numbers = [4, 1, 2, 1], target = 4>
Depth 0:                                  0
                                    /           \
Depth 1:                        -4                 +4
                              /     \           /       \
Depth 2:                  -1         +1      -1           +1
                         /  \       /  \     /  \         /  \
Depth 3:              -2    +2   -2    +2  -2    +2     -2    +2
                      / \   / \  / \   / \ / \   / \    / \   / \
Depth 4:           -1  +1 -1 +1 -1 +1-1 +1-1 +1 -1 +1 -1  +1 -1 +1


Depth 0:                          0
                               /     \
Depth 1:                   +4          -4
                          /  \         /  \
Depth 2:               +5     +3     -3    -5
                      /  \   /  \   /  \   /  \
Depth 3:            +7  +3 +1  +5 -1  -5 -3   -7

<결과>
[+4 +1 -2 +1] = 4  
[+4 -1 +2 -1] = 4  
→ 총 2가지 경우가 target과 일치하므로 return 값은 2
"""

# 초기 코드 - sum에 각 경로의 결과 합 저장(트리 그대로 유지)
def solution_init(numbers, target):
    answer = 0
    
    def dfs(currentNode, sum, level, numbers, target):
        # 중첩 함수 중 바깥 함수의 지역 변수 수정: nonlocal 키워드 필요
        nonlocal answer
        
        # 트리 끝(leaf node)에 도달해서 더이상 방문할 노드가 없을 때 함수 종료
        if level >= len(numbers)-1:
            sum += currentNode

            # 누적된 합이 target일 때 count 증가
            if sum == target:
                answer += 1
            return

        # print(f"Depth: {level}, 숫자: {nodeN}, 총합: {sum}")
        
        sum += currentNode
        
        # 왼쪽: -
        dfs(-numbers[level+1], sum, level+1, numbers, target)
        # 오른쪽: +
        dfs(numbers[level+1], sum, level+1, numbers, target)
        
    dfs(0, 0, -1, numbers, target)
    
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution_init(numbers, target))

numbers = [4, 1, 2, 1]
target = 2
print(solution_init(numbers, target))

print("------------------------------------------------------")

# 수정 코드 - 각 노드에 누적 합 저장
def solution(numbers, target):
    answer = 0

    def dfs(index, current_sum):
        # 중첩 함수 중 바깥 함수의 지역 변수 수정: nonlocal 키워드 필요
        nonlocal answer

        # 트리 끝(leaf node)에 도달해서 더이상 방문할 노드가 없을 때 함수 종료
        if index == len(numbers):
            if current_sum == target:
                answer += 1
            return

        # 왼쪽 -> -
        dfs(index + 1, current_sum + numbers[index])
        # 오른쪽 -> +
        dfs(index + 1, current_sum - numbers[index])

    dfs(0, 0)
    return answer
numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))

numbers = [4, 1, 2, 1]
target = 2
print(solution(numbers, target))