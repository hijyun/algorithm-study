import sys
n = int(input())
array = [int(x) for x in sys.stdin.readline().split()]
array_1 = list(set(array))
array_1.sort()

dic = dict((a,i) for i,a in enumerate(array_1))

for i in array:
    print(dic[i], end=' ')