## 18870

### 핵심
1. 1차 시도 -> 시간 초과
    * 배열의 복사본을 정렬한 후 각 원소가 정렬된 배열에서 가지는 인덱스 값을 이용
    * 인덱스 값을 찾는 알고리즘의 시간 복잡도가 O(n)이므로 전체 시간 복잡도가 O(n^2)
2. 2차 시도 -> 시간 초과
    * Scanner를 사용하여 입력을 받음
    * 반복문을 이용하여 결과를 출력
3. HashMap을 사용하여 각 원소가 정렬된 배열에서 가지게 되는 인덱스 값을 저장
4. BufferedReader와 StringTokenizer를 사용하여 입력을 받음
5. StringBuilder를 사용하여 결과를 출력
<br/>

### 사용
1. BufferedReader
2. StringTokenizer
3. StringBuilder
4. Arrays.sort()
