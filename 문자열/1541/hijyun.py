# https://sungmin-joo.tistory.com/67

arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    s += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)

'''
<그리디 알고리즘>
- 마이너스를 만날 때 가장 큰 수를 빼면 된다.
- 마이너스 기호를 만날 때 다음 마이너스 까지, 다음 마이너스가 없다면 끝까지 모든 수를 더해서 한 번에 빼 준다.
'''