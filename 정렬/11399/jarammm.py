n = int(input())
lst = list(map(int, input().split()))
lst.sort()
total = 0
for i in range(n):
    total += lst[i]*(n-i)
print(total)

'''
input
5
3 1 4 3 2
output
32
'''
