# 백준/정렬/1015

# 예제 3

N = input()
A = list(map(int, input().split()))
B = sorted(A)
for i, v in enumerate(A):
    A[i] = B.index(v)
    B[A[i]] = 0
print(*A)
