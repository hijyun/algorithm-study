n = int(input()) # 입력값
li = list(map(int, input().split()))
li_sorted = sorted(li) # 정렬
ans = []
for i in range(n):
    idx = li_sorted.index(li[i])
    ans.append(idx)
    li_sorted[idx] = -1 # 중복된 숫자가 있다면 앞 순서부터 -1로 변환
    
print(*ans) # *연산자는 리스트 unpacking 할 때 사용

# for i in ans:
#     print(i, end=" ")