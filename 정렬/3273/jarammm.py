n = int(input())
lst = list(map(int, input().split()))
num = int(input())
cnt = 0
lst.sort()

# two pointer
l, r = 0, n-1
while l != r:
    if lst[l] + lst[r] == num:
        cnt += 1
        l += 1
    elif lst[l] + lst[r] > num:
        r -= 1
    else:
        l += 1

print(cnt)

'''
input
9
5 12 7 10 9 1 2 3 11
13
output
3
'''

