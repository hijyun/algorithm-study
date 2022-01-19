# 문제 접근방법
* 중복을 제거하고 (set 이용) 정렬된 결과의 인덱스가 그 원소보다 작은 원소의 개수임.
* 처음엔 리스트 index 메서드를 이용하여 구현했는데 시간 초과됨.
* 딕셔너리를 이용해 구현하니 통과됨.

## 코드
* 시간 초과
```python
import sys

n = int(input())
array = [int(x) for x in sys.stdin.readline().split()]
array_1 = list(set(array))
array_1.sort()

for i in array:
    print(array_1.index(i), end=' ')
```

* 통과된 코드
```python
import sys

n = int(input())
array = [int(x) for x in sys.stdin.readline().split()]
array_1 = list(set(array))
array_1.sort()

dic = dict((a,i) for i,a in enumerate(array_1))

for i in array:
    print(dic[i], end=' ')
```