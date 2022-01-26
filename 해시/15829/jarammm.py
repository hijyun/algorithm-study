n = int(input())
s = input()
cnt = 0
for idx, v in zip(range(n), s):
    cnt += (ord(v)-96)*(31**idx)
print(cnt % 1234567891)

