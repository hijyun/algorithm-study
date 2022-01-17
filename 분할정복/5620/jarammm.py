# 브루트포스 : 시간 초과

points = []
d = 200000000
n = int(input())
for _ in range(n):
    points.append(list(map(int, input().split())))

for i in range(n - 1):
    x = points[i][0]
    y = points[i][1]
    for point in points[i + 1:]:
        d = min(pow(x - point[0], 2) + pow(y - point[1], 2), d)

print(d)

