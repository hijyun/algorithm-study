import heapq
# import sys
# input = sys.stdin.readline

N = int(input())
M = int(input())

G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append((c, b)) # (연결 비용, 연결된 컴퓨터)
    G[b].append((c, a))

q = [(0, 1)]
visited = [False] * (N + 1)
ans = 0

while q:
    cost, node = heapq.heappop(q) # heappop : 가장 작은 수부터 pop
    # 첫 q는 (0,1)로, 일단 노드 1 방문하고, 연결이 없으므로 cost는 0
    if not visited[node]:
        visited[node] = True
        ans += cost
        for x in G[node]: # 노드와 연결된 다른 노드를 꺼냄 / x = (cost,node) / x[1] = node
            if not visited[x[1]]:
                heapq.heappush(q, x) # q라는 리스트에 x(cost,node) 추가

print(ans)