n = int(input())
p = list(map(int, input().split()))
answer = 0

# 1. 정렬
p.sort()

# 2. 최소값 계산
for i in range(n):
    answer += p[i]     #i번쩨로 최소인 값 더하기
    for j in range(i):
        answer += p[j] #i보다 작은 번째로 최소인 값 전부 더하기

print(answer)