import sys, math

input = sys.stdin.readline

# switch[i]값을 반대로 바꿔주는 함수
def change(x):
    if x == 0:
        x = 1
    else:
        x = 0
    return x

'''start of main'''
n = int(input())
initial = [-math.inf] # -2147000000
temp = list(map(int, input().split())) # 켜짐: 1, 꺼짐: 0
switch = initial + temp # 1번 스위치 == index: 1에 위치하도록 하기 위함
student_count = int(input())
# 남: 1, 여: 2
for _ in range(student_count):
    gender, s = map(int, input().split()) # 성별, 받는 스위치개수
    if gender == 1: # 남학생일 경우
        for i in range(1, n+1):
            if i%s == 0:
                switch[i] = change(switch[i])

    else: # 여학생일 경우
        left = s-1
        right = s+1
        max_loop = int(n/2 + 0.5) -1
        switch[s] = change(switch[s])
        for _ in range(max_loop):
            # n=9-> 최대 4번, n=8-> 최대 3번([3, 5], [2, 6], [1, 7])
            if left == 0 or right == n+1:
                break
            if switch[left] == switch[right]: # 대칭이라면
                switch[left] = change(switch[left])
                switch[right] = change(switch[right])
                left -= 1
                right += 1
for i in range(1, n+1):
    if i%20 == 0:
        print(switch[i])
    else:
        if i == n:
            print(switch[i])
        else:
            print(switch[i], end=' ')
'''end of main'''

'''
<알고리즘 설명>
Step1. 각 학생마다 성별에 맞는 규칙으로 스위치 상태 변경
Step2. 최종으로 변경된 스위치 상태 출력

<수행시간 분석>
스위치의 개수를 n, 학생의 수를 m이라고 하면
Step1. O(n*m)
Step2. O(n)
=> 총 수행시간: O(n) + O(n*m) = O(n*m)
'''
