# 선택 정렬
n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
    
def selection_sort(lst):
    n = len(lst)
    for i in range(0,n-1):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
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

