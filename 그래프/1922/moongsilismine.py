"""
Kruskal Algorithm
- 시간 복잡도: O(ElogE)
- 정점에 비해 간선이 적은 희소 그래프에서 적합
- 과정
1. 그래프의 간선들을 가중치(비용)의 오름차순으로 정렬
2. 정렬된 간선 리스트에서 순서대로, 사이클을 형성하지 않는 간선을 선택
=> union-find자료구조 이용
3. 해당 간선을 현재의 MST의 집합에 추가

참고
-https://velog.io/@ready2start/Python-MST-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
-https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html
"""

def find_set(x):
    # x의 대표원소(부모)를 찾아서 리턴한다.
    while x != parents[x]:
        x = parents[x]
    return x


N = int(input()) #정점(컴퓨터)의 개수 (1번 ~ N번)
M = int(input()) #간선(연결할 수 있는 선)의 개수

edges = [] #그래프의 간선 정보

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a-1, b-1, c)) #parents 인덱스 접근을 위해 0부터 시작하도록 -1

# 1. 간선을 비용(c)순으로 오름차순 정렬
edges.sort(key=lambda x: x[2])

# parents : 각 정점의 부모 원소 (초기 설정: 모두 자기 자신)
# cnt : 찾은 간선의 개수
# min_cost : 모든 컴퓨터를 연결하는데 필요한 최소비용
parents = [x for x in range(N)]
min_cost, cnt = 0, 0

for a, b, c in edges:
    # 해당 간선이 사이클을 만들지 않는다면(부모가 다르면)
    if find_set(a) != find_set(b):
        # union 연산을 수행한다. (b의 대표 원소가 a의 대표 원소를 가리키게 한다.)
        parents[find_set(b)] = find_set(a)
        min_cost += c
        cnt += 1
        
        # N - 1개의 간선을 모두 찾은 경우, 탐색을 종료한다.
        if cnt >= N - 1:
            break

print(min_cost)