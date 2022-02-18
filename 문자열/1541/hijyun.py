# https://pacific-ocean.tistory.com/228

a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)

'''
<그리디 알고리즘>
- 마이너스를 만날 때 가장 큰 수를 빼면 된다.
- 마이너스 기호를 만날 때 다음 마이너스 까지, 다음 마이너스가 없다면 끝까지 모든 수를 더해서 한 번에 빼 준다.
'''