N = int(input())
A = list(map(int,input().split()))
B = sorted(A)
P = list()

for a in A:
    idx = B.index(a)
    B[idx] = 1001
    P.append(idx)
print(*P)

