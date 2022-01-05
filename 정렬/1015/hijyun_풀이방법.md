
# 문제 접근 방법
* 인덱스 이용. 
* 먼저 나온 값을 1001로 바꿔서 중복된 값이 나오지 않게하기.

```{python}
N = int(input())
A = list(map(int,input().split()))
B = sorted(A)
P = list()

for a in A:
    idx = B.index(a)
    B[idx] = 1001
    P.append(idx)
print(*P)

```