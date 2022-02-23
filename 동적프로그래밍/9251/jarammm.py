def lcs(m, n):  # m: length of x, n: length of y
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


dp = []
x = input()
y = input()
Y = [0]*(len(y) + 1)

for i in range(len(x)+1):
    dp.append(Y[:])  # dp.append(Y)하면 안됨! 주소 참조되어버림

ans = lcs(len(x), len(y))
print(ans)


# ACAYKP
# CAPCAK
# 4

