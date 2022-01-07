
# 문제 접근 방법
* 배열 정렬
* 가장 작은수와 가장 큰 수를 먼저 더하고, 왼쪽에서 조금씩 오른쪽에서 조금씩 숫자를 바꿔간다.

```{python}
n = int(input())
array = list(map(int, input().split()))
x = int(input())

array.sort()
left, right = 0, n - 1
count = 0
tmp = 0
while left != right:

    tmp = array[left] + array[right]

    if tmp == x:
        count += 1
        left += 1
    elif tmp > x:
        right -= 1
    else:
        left += 1

print(count)
```