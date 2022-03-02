'''
#출력 초과
N = int(input())
cards = []

for _ in range(N):
    cards.append(int(input()))

cards.sort()
sum = cards[0] + cards[1]
for i in range(2, N):
    sum += sum + cards[i]
    #10 20 20 20 30 => 10 + 20 = 30
    #20 20 30 => 30 + 20 = 50
    #20 30 => 50 + 20 = 70
    #30 => 70 + 30 = 100

print(sum)
'''
'''
#출력초과 again
#우선순위 큐 이용
#우선순위 큐: 데이터 추가 순서와 관계 없이, 데이터 제거는 가장 작은 값을 우선순으로 제거하는 자료구조
from queue import PriorityQueue

N = int(input())
que = PriorityQueue(maxsize=100000)

for _ in range(N):
    que.put(int(input()))

sum = que.get() + que.get()

while not que.empty():
    sum += sum + que.get()
    #10 20 20 20 30 => 10 + 20 = 30
    #20 20 30 => 30 + 20 = 50
    #20 30 => 50 + 20 = 70
    #30 => 70 + 30 = 100
    
print(sum)
'''
#정답 알고리즘
'''
0) 총 비교한 횟수(answer)를 0으로 둔다.
1) 현재의 카드 묶음(card_deck) 중 가장 작은 2개의 카드 묶음을 꺼낸다.
2) 두 개를 더한 값 = 현재 단계에서 비교한 횟수
3) 두 개를 더한 값을 총 비교한 횟수에 더해준다.
4) 두 개를 더한 값을 다시 카드 더미 안에 넣는다.
5) 1 ~ 4 과정을 힙에 하나의 덱만 남을 때 까지 반복한다.
'''
import heapq
import sys

N = int(input())
card_deck = []
for _ in range(N):
    heapq.heappush(card_deck, int(sys.stdin.readline()))


if len(card_deck) == 1: #1개일 경우 비교하지 않아도 된다
    print(0)
else:
    answer = 0
    while len(card_deck) > 1: #1개일 경우 비교하지 않아도 된다
        temp_1 = heapq.heappop(card_deck) #제일 작은 덱
        temp_2 = heapq.heappop(card_deck) #두번째로 작은 덱
        answer += temp_1 + temp_2 #현재 비교 횟수를 더해줌
        heapq.heappush(card_deck, temp_1 + temp_2) #더한 덱을 다시 넣어줌
        #10 20 20 20 30 => 10 + 20 = 30
        #20 20 30 30 => 20 + 20  = 40
        #30 30 40  => 30 + 30 = 60
        #40  60 => 40 + 60 = 100
        #100
    print(answer)