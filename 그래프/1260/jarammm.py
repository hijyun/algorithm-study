from collections import deque

'''
입력:
5 5 3
5 4
5 2
1 2
3 4
3 1
출력:
3 1 2 5 4 
3 1 4 2 5 
'''

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())
# 각 노드가 연결된 정보를 표현 (2차원 리스트)
g = [[] for _ in range(N+1)]
for _ in range(M):
    i,j = map(int, input().split())
    g[i].append(j)
    g[j].append(i)
for i in range(N+1):
    g[i] = sorted(g[i])

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False]*(N+1)
# 정의된 DFS 함수 호출
dfs(g, V, visited)
print()
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False]*(N+1)
bfs(g, V, visited)

