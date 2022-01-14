array = []
N = int(input())
for _ in range(N):
    array.append(int(input()))

for i in range(N-1):
    min_index = i
    for j in range(i + 1,N):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]


for i in range(N):
    print(array[i])
