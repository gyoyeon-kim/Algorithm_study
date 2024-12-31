def makeone(n):
    # 최소 연산 횟수를 저장하는 리스트
    dp = [0] * (n + 1)

    # 1부터 n까지 최소 연산 횟수를 계산
    for i in range(2, n + 1):
        # 기본적으로 1을 빼는 경우
        dp[i] = dp[i - 1] + 1
        # 2로 나눌 수 있는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        # 3으로 나눌 수 있는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]

N = int(input())
print(makeone(N))
