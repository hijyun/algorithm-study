#참고: https://pacific-ocean.tistory.com/228
#처음 나온 -바로 뒤에다가 괄호하는 것이 가장 작은 수가 나오게 되는 방법을 이용
#식 55 - 50 + 40 - 30 + 20 에서
#괄호를 55 - (50 + 40) - (30 + 20) 이렇게 하는 것이 최솟값
a = input().split('-') #-기호를 중심으로 분리하여 리스트에 저장
num = [] #숫자 저장할 리스트

for i in a:
    cnt = 0
    s = i.split('+') #+기호를 중심으로 분리
    for j in s:
        cnt += int(j) #숫자 덧셈
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i] #뺄셈 수행
print(n)