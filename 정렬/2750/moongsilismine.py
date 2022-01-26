#맞았습니다!! 30864kb, 128ms
N = int(input())
l = []

for i in range(N):
    l.append(int(input()))
    
#선택정렬
#1. 주어진 리스트 중에 최소값 찾기
#2. 그 값을 맨 앞에 위치한 값과 교환
#3. 맨 처음 위치를 뺀 나머지 리스트에 대해서 1, 2방법을 계속 교환

for i in range(N):
    #1. 주어진 리스트 중에 최소값 찾기
    m = min(l[i:]) #3. 맨 처음 위치를 뺀 나머지 리스트에 대해서 1, 2방법을 계속 교환
    #2. 그 값을 맨 앞에 위치한 값과 교환
    tmp = l[i]
    l[l.index(m)] = tmp
    l[i] = m
    
for i in range(N):
    print(l[i])