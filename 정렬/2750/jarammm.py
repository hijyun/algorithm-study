N = int(input())
n = []
for _ in range(N):
    n.append(int(input()))

for i in range(1, N):
    j = i-1
    new = n[i]
    while j >= 0 and new < n[j]:
        n[j+1] = n[j]
        j -= 1
    n[j+1] = new

for k in n:
    print(k)

