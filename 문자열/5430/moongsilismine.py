#https://hongcoding.tistory.com/44
import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip() #rstrip(): 문자열에서 공백 제거
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",") #대괄호 떼고, ","로 원소를 구분하여 저장
    queue = deque(arr) #앞뒤로 pop이 가능한 deque로 배열 저장
    
    rev = len(queue)-1 #R함수 실행 횟수 체크, 매번 reverse하면 시간초과 발생하여, 횟수 체크하여 나중에 한번에 뒤집기
    flag = 0 #에러 체크(에러 없으면 0, 있으면 1)
    if n == 0: #배열에 아무 원소도 없으면, 빈 큐
        queue = []
        
    for p_fun in p:
        if p_fun == 'R':
            rev += 1
        elif p_fun == 'D':
            if len(queue) < 1: #큐에 원소가 없으면
                flag = 1 #원소 제거를 못하므로 에러
                print("error")
                break
            else:
                if rev % 2 == 0: #안뒤집은 거나 동일. 맨 앞 원소 제거
                    queue.popleft()
                else: #뒤집은 상태이므로, 맨 뒤 원소 제거
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0: #뒤집을 필요 없음
            print("[" + ",".join(queue) + "]") #큐 원소들을 ,으로 조합해서 리스트 처럼 출력
        else:
            queue.reverse() #뒤집기
            print("[" + ",".join(queue) + "]")