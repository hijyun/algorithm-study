# 풀이 1 : 나의 풀이

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

if n < 3:
    print(n-1)
else:
    lst = sorted(lst, reverse=True); lst = lst[:-2]+[sum(lst[-2:])]; ans = 0
    for i in range(n-1):
        ans += lst[i]*2**i
    print(ans)


# 풀이 2 : https://velog.io/@dding_ji/baekjoon-1715

import heapq
'''
heap
1. 모든 부모 노드가 자식보다 작거나 같은 값을 갖는 이진 트리이며 가장 작은 값은 언제나 heap[0]임
2. 이러한 구조를 유지하는 것을 힙의 불변성이라함
'''

n = int(input())
card = [int(input()) for _ in range(n)]
heapq.heapify(card)  # heapq.heapify(리스트) : 리스트 x를 선형 시간으로 제자리에서 힙으로 변환
answer = 0

while len(card) > 1:  # card 묶음이 2개 이상이어야만 비교가 가능
    a = heapq.heappop(card)  # heapq.heappop(리스트) : 힙 불변성을 유지하면서, heap에서 가장 작은 항목을 팝하고 반환
    b = heapq.heappop(card)
    answer += a + b
    heapq.heappush(card, a + b)  # heapq.heappush(heap, item) : 힙 불변성을 유지하면서, item 값을 heap으로 푸시

print(answer)

