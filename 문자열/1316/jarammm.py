n = int(input())
cnt = n
for _ in range(n):
    pattern = input()
    now = [pattern[0]]
    for i in pattern:
        if i != now[-1]:
            if i in now:
                cnt -= 1
                break
            else:
                now.append(i)
print(cnt)