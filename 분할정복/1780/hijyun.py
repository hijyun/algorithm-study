#https://velog.io/@uoayop/BOJ-1780-%EC%A2%85%EC%9D%B4%EC%9D%98-%EA%B0%9C%EC%88%98Python
import sys
input = sys.stdin.readline

n = int(input())
minus_cnt, zero_cnt, plus_cnt = 0, 0, 0

papers = []
for _ in range(n):
    row = list(map(int, input().rsplit()))
    papers.append(row)


def check(row, col, n):
    global minus_cnt, zero_cnt, plus_cnt
    curr = papers[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if papers[i][j] != curr:
                next_n = n // 3
                check(row, col, next_n)  # 1
                check(row, col + next_n, next_n)  # 2
                check(row, col + (2 * next_n), next_n)  # 3
                check(row + next_n, col, next_n)  # 4
                check(row + next_n, col + next_n, next_n)  # 5
                check(row + next_n, col + (2 * next_n), next_n)  # 6
                check(row + (2 * next_n), col, next_n)  # 7
                check(row + (2 * next_n), col + next_n, next_n)  # 8
                check(row + (2 * next_n), col + (2 * next_n), next_n)  # 9
                return

    if curr == -1:
        minus_cnt += 1
    elif curr == 0:
        zero_cnt += 1
    elif curr == 1:
        plus_cnt += 1
    return


check(0, 0, n)

print(minus_cnt)
print(zero_cnt)
print(plus_cnt)