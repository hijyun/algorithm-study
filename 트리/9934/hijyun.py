K=int(input())
array = list(map(int,input().split()))
trees = [[] for _ in range(K)]

def binary_search(array, K):
    if len(array)==1:
        trees[K].extend(array)
        return
    mid = len(array) // 2
    trees[K].append(array[mid])
    binary_search(array[:mid],K+1)
    binary_search(array[mid+1:],K+1)

binary_search(array,0)

for i in range(K):
    if i==0:
        print(trees[i][0])
    else:
        print(*trees[i])


