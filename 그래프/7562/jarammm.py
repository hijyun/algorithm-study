from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(sx, sy, ax, ay):
    if ax==sx and ay==sy:
        print(0)
        return
    q = deque()
    q.append([sx, sy])
    s[sx][sy] = 1
    while q:
        a, b = q.popleft()
        for i, j in zip(dx,dy):
            x = a + i
            y = b + j
            if 0 <= x < n and 0 <= y < n and s[x][y] == 0:
                if [x,y] == [ax,ay]:print(s[a][b]);q = 0;break;
                q.append([x, y])
                s[x][y] = s[a][b] + 1

t = int(input())
for i in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    ax, ay = map(int, input().split())
    s = [[0] * n for i in range(n)]
    bfs(sx, sy, ax, ay)
