N, K = map(int, input().split())
A = list(map(int, input().split()))
swap = [-1]
cnt = 0
for i in range(N, 1, -1):
    last = A.index(max(A[:i]))
    if last != i-1:
        cnt += 1
        A[i-1], A[last] = A[last], A[i-1]
        if cnt == K:
            swap = sorted([A[last], A[i-1]])
            break
print(*swap)
