L = int(input())
chars = input()
sum = 0

for i,char in enumerate(chars):
    sum += ord(char) % 96 * 31 ** i
    if sum > 1234567891:
        sum %= 1234567891

print(sum)


# 더 나은 풀이
L = int(input())
chars = input()
sum = 0

for i,char in zip(range(L), chars):
    sum += ord(char) % 96 * 31 ** i

print(sum % 1234567891)
