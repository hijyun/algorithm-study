import sys
S1 = sys.stdin.readline().strip().upper()
S2 = sys.stdin.readline().strip().upper()
len1 = len(S1)
len2 = len(S2)

# 길이 저장 공간 생성
matrix = [[0] * (len2 + 1)] * (len1 + 1)

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if S1[i - 1] == S2[j - 1]: #같을 경우, 현재 위치의 대각선 위 값에서 +1
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else: #다른 경우, 현재 위치의 한칸 위 또는 아래 중 큰 값
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1]) #마지막 값에서 모든 길이가 계산되므로 출력

#출처: https://suri78.tistory.com/11 [공부노트]