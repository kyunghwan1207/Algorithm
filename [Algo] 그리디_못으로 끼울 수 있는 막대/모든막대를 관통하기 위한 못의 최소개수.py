import sys
n = int(sys.stdin.readline())
L = []
for _ in range(n):
	a, b = map(int, sys.stdin.readline().split())
	L.append([a, b])
L.sort(key=lambda x : [x[1], x[0]]) # b기준 정렬 후 a기준 정렬
S = []
F = []
for i in range(n):
	S.append(L[i][0])
	F.append(L[i][1])
k = L[0][1] # 가장최근 막대의 끝점을 저장
cnt = 1
for i in range(1, n):
	if k < S[i]:
		cnt += 1
		k = F[i]
print(cnt)

'''
<알고리즘 설명>
모든 막대를 박을수 있는 최소의 못의 개수를 구할때, 막대의 끝점에만 못이 박히더라도 최소 개수의 못을 사용할 수 있다는 아이디어에서 시작했습니다.
왜냐하면 어차피 끝점을 기준으로 오름차순 정렬할 것이기 때문에 현재 막대 이후에 오는 막대들의 끝점은 같거나 큰 값들일 것입니다.
그렇기에 이제 고려해야할 것은 다음에 오는 막대의 시작점을 고려해야하기 때문에
현재막대의 끝점(k)을 유지하고 다음에 오는 막대의 시작점이 k보다 크다면 현재의 못 만으로는 다음의 막대를 박을 수 없기에 새로운 못이 필요합니다(cnt++).
정리하면 아래와 같습니다.
Step 1. 막대의 끝점(b)을 기준으로 오름차순정렬을 하고, 만약 끝점이 같다면 시작점(a)을 기준으로 오름차순정렬합니다.
Step 2. 시작점(a)과 끝점(b)을 각각 모은 리스트인 S, F에 Step 1에서 정렬한 순서대로 삽입합니다.
Step 3. 현재 유지하고 있는 막대의 끝점(k) 보다 큰 시작점(S[i])을 가진 막대가 등장하면 추가적인 못이 필요하므로 cnt ++ 한 후, k = F[i]로 업데이트 합니다.
Step 4. i < n 일 동안 Step 3 반복수행합니다.

<수행시간 분석>
막대의 갯수를 n이라고 하면
Step 0. 시작점(a), 끝점(b)입력받기 -> O(n)
Step 1  -> O(nlogn)
Step 2  -> O(n)
Step 3,4 -> O(n)
=> 총 수행시간: O(nlogn)
'''
