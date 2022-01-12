### 문제 접근 방법
* 일반적인 선택 정렬은 처리할 대상 범위에서 최솟값을 찾아 그 값과 범위의 맨 앞에 있는 값을 서로 바꾸는 과정을 반복합니다. 이 과정이 한 번 끝날 때마다 범위 안의 맨 앞에 있는 값은 정렬이 끝난 것이므로 정렬 대상 범위에서 제외합니다.

* 선택 정렬 기본 개념 사용
```
def sel_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(a)     # 정렬 과정 출력하기

 

d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)

```
