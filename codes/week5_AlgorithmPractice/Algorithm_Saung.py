def calculate(matrix, hidden, n, m, k, is_all_even):
    # 각 열마다 [보이는 면의 총합, 숨겨진 면의 총합]을 저장
    col_sum = [[0, 0] for _ in range(m)]

    # 각 열의 합을 계산
    for i in range(n):
        for j in range(m):
            col_sum[j][0] += matrix[i][j]    # 보이는 면의 값 더하기
            col_sum[j][1] += hidden[i][j]    # 숨겨진 면의 값 더하기

    # 점수 초기화
    res = 0

    # 열마다 "보이는 면 합 vs 숨겨진 면 합 - 비용" 중 큰 값을 더함
    for j in range(m):
        res += max(col_sum[j][0], col_sum[j][1] - k)

    # 격자가 짝수 x 짝수일 경우, 중복 점수를 보정하기 위해 최소값 하나를 뺌
    if is_all_even:
        min_val = float('inf')  # 최소값 초기화
        for i in range(n):
            for j in range(m):
                if (i + j) % 2 == 0:
                    continue  # 체스판의 흰칸은 스킵하고 검정칸만 검사

                # 보이는 합과 숨겨진 합이 같은 경우
                if col_sum[j][0] == col_sum[j][1] - k:
                    val = min(matrix[i][j], hidden[i][j])
                # 보이는 면을 선택한 경우
                elif col_sum[j][0] > col_sum[j][1] - k:
                    val = matrix[i][j]
                # 숨겨진 면을 선택한 경우
                else:
                    val = hidden[i][j]

                # 가장 작은 점수값 갱신
                min_val = min(min_val, val)

        # 점수를 과다하게 더했을 가능성이 있으므로 최소값 하나를 빼서 보정
        res -= min_val

    return res


def solution(visible, hidden, k):
    import copy

    n = len(visible)      # 행 수
    m = len(visible[0])   # 열 수

    # 격자가 짝수 x 짝수 크기인지 확인
    is_all_even = n % 2 == 0 and m % 2 == 0

    cases = 1 << n  # 가능한 모든 행 뒤집기 조합 (2^n)
    res = 0         # 최대 점수를 저장할 변수

    # 모든 행 뒤집기 조합을 순회
    for i in range(cases):
        # visible과 hidden을 얕은 복사 (각 행 자체는 그대로 사용됨)
        v_copy = visible[:]
        h_copy = hidden[:]
        cost = 0  # 이 조합에서 발생하는 뒤집기 비용

        # j번째 행을 뒤집을지 여부 판단 (비트마스킹)
        for j in range(n):
            if i & (1 << j):
                # 행을 뒤집는다면 보이는 면과 숨겨진 면을 교환
                v_copy[j], h_copy[j] = h_copy[j], v_copy[j]
                cost += k  # 뒤집기 비용 추가

        # 현재 조합에 대해 열을 greedy하게 계산한 점수에서 비용을 뺀 값
        score = calculate(v_copy, h_copy, n, m, k, is_all_even) - cost

        # 지금까지 중 가장 높은 값으로 갱신
        res = max(res, score)

    return res
