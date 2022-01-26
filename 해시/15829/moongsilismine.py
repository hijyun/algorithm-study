L = int(input())
string = list(map(ord, input())) #ord(): 문자열 -> 숫자 아스키 변환 함수. 소문자는 a=97부터. 대문자는 A=65
H = 0

for i in range(len(string)): #zip쓰면 좀 더 빠르다고 한다.
    H += (string[i]-96)*31**i #문제의 공식 구현

print(H % 1234567891) #마지막에 나머지구하면 됨. for문에서 계속하면 틀림.