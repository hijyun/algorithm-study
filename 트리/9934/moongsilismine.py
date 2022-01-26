n = int(input())

tree = list(map(int, input().split()))
level = [[] for _ in range(n)]

def sol(s, e, depth):
    if s==e:
        level[depth].append(tree[s])
        return
    root = (s+e)//2 # 인덱스의 중간에 있는 값이 루트노드
    level[depth].append(tree[root]) # 레벨을 인덱스로 삼아 그 레벨에 있는 노드들을 더해준다.
    sol(s, root-1, depth + 1) # 왼쪽 하위 서브트리를 다시 순회, 깊이를 늘려주면서 재귀호출
    sol(root+1, e, depth + 1) # 오른쪽 하위 서브트리를 다시 순회, 깊이를 늘려주면서 재귀호출

sol(0,len(tree)-1,0)

for i in level:
    for j in i:
        print(j, end=" ")
    print()