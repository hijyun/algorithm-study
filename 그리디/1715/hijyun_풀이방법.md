# 접근 방법
* 카드를 정렬한 후에 
* 작은 것 부터 두개씩 더한 후 더한 값에 다시 반복</br>

<br>

# 풀이 방법

* 리스트를 사용했을 때 시간초과
```python
import sys
n = int(sys.stdin.readline().rstrip())
card = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
card.sort()

answer = 0

while True:
    if n >= 2:
        num1 = card.pop(0)
        num2 = card.pop(0)
        answer += (answer + num1 + num2)
        n -= 2
    elif n == 1:
        break
answer += (answer + card.pop())

print(answer)
```
<br>

* 우선순위 큐를 사용하여 통과. 파이썬 heapq모듈을 import 하여 사용
```python
import heapq # 우선순위 큐

N = int(input())

cardList = list(int(input()) for _ in range(N))
heapq.heapify(cardList)
result=0


while len(cardList) != 1:
    num1 = heapq.heappop(cardList)
    num2 = heapq.heappop(cardList)
    Sum = num1 + num2
    result += Sum
    heapq.heappush(cardList,Sum)

print(result)
```