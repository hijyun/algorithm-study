# 중위 순회, DFS
# 참고 : https://westmino.tistory.com/28


n = int(input())  # 트리의 깊이
nums = list(map(int, input().split())) # 방문한 순서대로의 빌딩 번호 리스트
num_idx = 0 # 빌딩 방문 리스트의 인덱스 변수. 0번째 부터 순차적으로 방문하므로 0으로 초기화.
tree = [[] for _ in range(n)]

def solv():
    inorder(0)
    for row in tree:
        print(*row)

def inorder(depth):
    global tree,num_idx
    if depth == n: # 깊이가 채워지면 함수 빠져나옴
        return

    # 왼쪽 노드 순회
    inorder(depth+1)
    # 루트 노드 순회
    tree[depth].append(nums[num_idx]) # depth층에 num_idx번째 방문한 빌딩 번호를 추가
    print(nums[num_idx],"번 빌딩 방문 추가, ",depth+1, "층", tree[depth])
    num_idx += 1
    # 오른쪽 노드 순회
    inorder(depth+1)  # 17행과 차이점 : num_idx += 1

solv()

'''
Input:
3
1 6 4 3 5 2 7
Output:
1 번 빌딩 방문 추가,  3 층 [1]
6 번 빌딩 방문 추가,  2 층 [6]
4 번 빌딩 방문 추가,  3 층 [1, 4]
3 번 빌딩 방문 추가,  1 층 [3]
5 번 빌딩 방문 추가,  3 층 [1, 4, 5]
2 번 빌딩 방문 추가,  2 층 [6, 2]
7 번 빌딩 방문 추가,  3 층 [1, 4, 5, 7]
3
6 2
1 4 5 7
'''
