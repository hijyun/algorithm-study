n, k = map(int, input().split())
s = list(map(int, input().split()))
s.sort()	#입력받은 리스트를 정렬
print(s[k - 1])	#정렬된 리스트에서 k번째 수 출력