n = int(input())
for _ in range(n):
    style, pattern = input().split()
    if style == "1":
        # 각 숫자를 이진수 변환 후, 문자열로 이어붙이기
        pattern = pattern.split('.')
        num = ""
        for i in pattern:
            num += '{0:08b}'.format(int(i))
        # 문자열로 표현된 이진수를 숫자 십진수로 변환
        num = int(num, 2)  # 십진수로 변환하되 변환하려는 숫자는 원래 2진수라는 의미
        print(num)
    else:
        # 주소를 이진수로 나타내면 숫자가 64개
        pattern = '{0:064b}'.format(int(pattern))
        num = f"{int(pattern[:8], 2)}"
        for i in range(8, len(pattern), 8):
            num += f".{int(pattern[i:i + 8], 2)}"
        print(num)

# 3
# 1 70.236.217.197.157.238.150.80 -> 5110699119940114000
# 2 5110699119940114000 -> 70.236.217.197.157.238.150.80
# 2 0 -> 0.0.0.0.0.0.0.0
