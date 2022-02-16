N = int(input())

group_cnt = N

for _ in range(N):
    word = input()
    group = []
    front = word[0]
    for w in word:
        if w in group: #현재 확인하는 단어가 그룹에 있으면
            if front == w: #앞에있는 단어이면, 연속해서 나오는 중이므로 계속
                continue
            else: #그렇지 않으면, 떨어져서 나타난 단어이므로 그룹단어가 아님
                group_cnt -= 1
                break
        else: #현재 확인하는 단어가 그룹에 없으면
            group.append(w) #그룹에 추가
            front = w #앞에 있는 단어를 현재 단어로 변경

print(group_cnt)