# 코드 참고: https://goplanit.site/42.%20Algorithm(1260_py)/

# Depth First Search
def dfs(n):
    print(n, end=' ')
    visited[n] = True #정점을 방문하면, 방문여부 true
    for i in graph[n]: #현재 정점과 연결된 다른 정점들 중에
        if not visited[i]: #방문되지 않은 정점이면 계속dfs
            dfs(i)

# Breadth First Search
def bfs(n):
    visited[n] = True #정점을 방문하면, 방문여부 true
    queue = deque([n]) #현재 정점을 큐에 추가
    while queue: #큐가 비어있지 않으면
        v = queue.popleft() #큐에 있는 정점을 뽑는다
        print(v, end= ' ') #방문
        for i in graph[v]: #이 정점과 연결된 다른 정점들 중에
            if not visited[i]: #방문되지 않은 정점이면
                queue.append(i) #큐에 추가
                visited[i] = True #방문

import sys
from collections import deque

# node, branch, first node
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

# make adjacency list
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# sort adjacency list
for i in range(1, n+1):
    graph[i].sort()

dfs(v)
# initialize check list
visited = [False] * (n + 1)
print()
bfs(v)
#알고리즘
#algorithm
