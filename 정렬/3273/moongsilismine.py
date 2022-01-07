#입력
n = int(input())
a = list(map(int, input().split()))
x = int(input())

#정답용 변수
answer = 0

'''틀린 코드: 시간초과
for i in range(n):
    for j in range(1, n):
        if i < j:
            if a[i] + a[j] == x:
                answer += 1
'''

#1. 오름차순 정렬
a_sort = sorted(a)

#2. 투 포인터 (개념 참고: https://butter-shower.tistory.com/226)
# 1) 포인터 선언
i = 0
j = n-1

# 2) 포인터 움직이기
while (i < j): #i, j포인터가 교차되면 반복 종료
    # 2-1) 현재 합이 x와 같으면 i, j포인터 동시 이동
    if a_sort[i] + a_sort[j] == x:
        answer += 1
        i += 1
        j -= 1 # n개의 서로다른 양의 정수로 이뤄진 수열이므로, 현재 포인터가 위치한 값들이 또 나올일은 없으므로, 두개의 포인터를 동시 이동시켜도 됨.
    # 2-2) 현재 합이 x보다 크면 j포인터만 이동
    elif a_sort[i] + a_sort[j] > x:
        j -= 1
    # 2-3) 현재 합이 x보다 작으면 i포인터만 이동
    else:
        i += 1     

print(answer)