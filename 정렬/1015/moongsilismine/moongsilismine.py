n = int(input())
t = list(map(int, input().split()))	#map으로 입력된 리스트 원소 값을 모두 int형으로 변환

s_li = sorted(t)	#t를 오름차순 정렬
li = []

for i in range(n):
    idx = s_li.index(t[i])	#정렬되지 않은 t의 첫번째 원소가 s_li에서의 index
    li.append(idx)
    s_li[idx] = -1

print(*li)	#리스트값을 원소만 출력하게