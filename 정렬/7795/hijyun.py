for _ in range(int(input())):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    result = 0
    for a in A:
        count = 0
        start, end = 0, M-1
        while start <= end:
            mid = (start + end) // 2
            if B[mid] < a:
                count = (mid+1)
                start = mid + 1
            else:
                end = mid - 1

        result += count
    print(result)