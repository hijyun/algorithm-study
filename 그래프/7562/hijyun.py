# 참고 : https://bang-tori.tistory.com/m/27
from collections import deque
import sys

input = sys.stdin.readline

t = int(input().rstrip())

def bfs():
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]

    q = deque()
    q.append((startX, startY))
    while q: # 큐가 빌 때 까지 while문 실행
        x, y = q.popleft() # 현재 위치
        if x == endX and y == endY: # 목적지 도착
            return matrix[x][y] - 1 # 1부터 시작했으니까 1빼기
        for i in range(8): # 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and matrix[nx][ny] == 0: # 체스판 내에서 방문한 적이 없으면
                matrix[nx][ny] = matrix[x][y] + 1 # 방문 처리
                q.append((nx, ny))


for _ in range(t):
    l = int(input().rstrip()) # 체스판 크기
    startX, startY = map(int, input().rstrip().split()) # 시작 위치
    endX, endY = map(int, input().rstrip().split()) # 목적 위치
    matrix = [[0] * l for _ in range(l)] # 체스판
    matrix[startX][startY] = 1 # 이동 횟수 세기
    print(bfs())