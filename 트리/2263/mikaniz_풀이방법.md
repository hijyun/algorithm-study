## 2263

### 핵심
1. postorder의 가장 끝 값이 해당 트리의 루트 노드
2. 해당 트리의 루트 노드를 출력한 후 왼쪽 서브 트리, 오른쪽 서브 트리로 이동하여 같은 명령을 수행하는 재귀 함수 사용
3. 1차 시도 -> 시간 초과
    * inorder에서 루트 노드의 index를 찾기 위해 ArrayList.indexOf() 사용
    * 해당 함수의 시간 복잡도가 O(n)이므로 전체 시간 복잡도가 O(n^2)
4. inorder에서 루트 노드의 index를 찾기 위해 각 노드의 index를 저장하는 배열 생성
<br/>

### 사용
1. BufferedReader
2. StringTokenizer
