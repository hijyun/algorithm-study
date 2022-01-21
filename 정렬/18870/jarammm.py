N = int(input())
nums = list(map(int, input().split()))
nums_set = list(sorted(set(nums)))  # 중복 제거 후 오름차순 정렬 리스트
nums_set = {nums_set[i]: i for i in range(len(nums_set))}  # 가장 작은 수에 0, 그 다음 수에 1,... value 부여
print(*[nums_set[i] for i in nums])

'''
예제 입력 1
5
2 4 -10 4 -9  --> nums_set = [-10, -9, 2, 4] --> nums_set = {-10:0, -9:1, 2:2, 4:3}

예제 출력 1
2 3 0 3 1     --> [nums_set[2], nums_set[4], nums_set[-10], nums_set[4], nums_set[-9]]
'''

