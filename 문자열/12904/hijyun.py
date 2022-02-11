s = list(input()) # 문자열 S
t = list(input()) # 문자열 t

success = False # 성공 여부 체크

while len(s) != len(t):
    if t[-1] == 'A': # 규칙 1
        t.pop()
    elif t[-1] == 'B': # 규칙 2
        t.pop()
        t = t[::-1]
    if s == t: # 성공 체크
        success = True

if success:
    print(1)
else:
    print(0)