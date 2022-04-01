import sys
input = sys.stdin.readline

def rotate(t):
    global n, m, arr
    # 꺾이는 부분의 값을 별도로 저장
    top = arr[t][t] # 상
    left = arr[n-1-t][t] # 좌
    bottom = arr[n-1-t][m-1-t] # 하
    right = arr[t][m-1-t] # 우
    # 상 회전
    for i in range(t+1, m-t):
        arr[t][i-1] = arr[t][i]
    # 좌 회전
    for i in range(n-2-t, t-1, -1):
        arr[i+1][t] = arr[i][t]
    # 하 회전
    for i in range(m-2-t, t-1, -1):
        arr[n-1-t][i+1] = arr[n-1-t][i]
    # 우 회전
    for i in range(t+1, n-t):
        arr[i-1][m-1-t] = arr[i][m-1-t]
    # 꺾이는 값을 회전 후 적절한 곳에 저장
    arr[t+1][t] = top
    arr[n-1-t][t+1] = left
    arr[n-2-t][m-1-t] = bottom
    arr[t][m-2-t] = right
    
'''start of main'''
n, m, r = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
for _ in range(r):
    for i in range(min(n, m)//2): # n x m 행렬일 때, 최소값의 절반 개수만큼의 세트만 회전시키면 된다.
        rotate(i)

for i in range(n):
    if i != 0:
        print()
    for j in range(m):
        print(arr[i][j], end =' ')
'''end of main'''

'''
<알고리즘 설명>
Step1. 사용할 변수 및 배열 할당
Step2. rotate함수 호출
Step3. 꺾이는 값을 별도로 저장한 후 상,하,좌,우를 각 회전한 후 다시 꺾이는 값을 배열의 적절한 위치에 저장
Step4. 배열원소 출력

<수행시간 분석>
배열의 크기를 n x m 이라고 하고, 회전 횟수를 r이라고 하면
Step1. O(n)
Step2,3. O(r*m*n)  
(이유: rotate함수의 호출횟수는 min(n,m) 만큼 반복되고, rotate함수 내부적으로 수행시간을 결정하는 것은 max(n,m)이므로 -> n과 m의 최댓값, 최솟값이 각각 수행시간에 영향을 끼침)
Step4. O(n*m)
=> 총 수행시간: O(n) + O(r*n*m) + O(n*m) = O(r*n*m)
'''
