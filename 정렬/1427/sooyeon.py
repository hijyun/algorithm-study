n = input()
num = [int(i) for i in n]
# num = sorted(num, reverse=True)
num.sort(reverse=True)

for i in num:
    print(i,end='')



## 2
n = input()
m = []
for i in range(len(n)):
    m.append(n[i])
m.sort(reverse=True)

for i in m:
    print(i, end='')