# 선택 정렬

n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
    
def selection_sort(lst):
    n = len(lst)
    for i in range(0,n-1): # 0부터 n -2까지 반복
        # i번 위치부터 끝까지 자료 값 중 최솟값의 위치를 찾음
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        # 찾은 최솟값을 i번 위치로 swap
        lst[i], lst[min_idx] = lst[min_idx], lst[i] # 변수에 대입된 값을 교환
        # print(lst)     # 정렬 과정 출력하기
    print(*lst)
    
selection_sort(m)


# sort 라이브러리 사용
def sel_sort():    
    n = int(input())
    lst = []
    for i in range(n):   # 배열로 입력
        lst.append(int(input()))
    lst.sort()  # 정렬
    for i in range(len(lst)):
        print(lst[i])
        
        
sel_sort()

