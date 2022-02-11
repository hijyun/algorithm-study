* 기본 아이디어 
  * S의 길이 <= T의 길이 이므로
  * S가 T가 되었는지 확인하는 것보다 T가 S가 되는지 확인하면 더 쉽게 풀림
  
* 규칙 변경
  * 문자열 뒤에 A를 추가한다 -> 마지막 문자열이 A라면 A를 제거한다.
  * 문자열을 뒤집고 뒤에 B를 추가한다. -> 마지막 문자열이 B라면 B를 제거하고, 문자열을 뒤집는다.
  
```python
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
```