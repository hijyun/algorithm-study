n = int(input())
array = list(map(int, input().split()))
x = int(input())

array.sort()
left, right = 0, n - 1
count = 0
tmp = 0
while left != right:
    tmp = array[left] + array[right]
    if tmp == x:
        count += 1
        left += 1
        right -= 1
    elif tmp > x:
        right -= 1
    else:
        left += 1

print(count)