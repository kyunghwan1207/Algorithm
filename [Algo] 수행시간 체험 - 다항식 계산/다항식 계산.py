import time, random

def evaluate_n2(A, x):
	# code for O(n^2)-time function
    n = len(A)
    result = 0
    for i in range(n):
        power_term = 1
        for j in range(i):
            power_term *= x
        result += A[i]*power_term
    return result
# end of evaluate_n2
	
def evaluate_n(A, x):
	# code for O(n)-time function
    n = len(A)
    result = 0
    power_term = x
    for i in range(n-1):
        A[i+1] = A[i+1]*power_term
        power_term *= x
    # A 리스트에 x까지 계산한 term으로 바꾼다
    for j in range(n):
        result += A[j]
    return result
# end of evaluate_n

random.seed()		# random 함수 초기화
# n 입력받음
n = int(input()) # 1000 ~ 100000 다양하게 바꿔가면서 측정해보자
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
## 찐
x = random.randint(-1000, 1000)
A = [random.randint(-1000, 1000) for _ in range(n)]

# evaluate_n2 호출
start_n2 = time.process_time()
print('evaluate_n2(A,x): ', evaluate_n2(A, x))
# evaluate_n2(A, x)
end_n2 = time.process_time()

# evaluate_n 호출
start_n = time.process_time()
print('evaluate_n(A,x): ', evaluate_n(A, x))
# evaluate_n(A, x)
end_n = time.process_time()

# 두 함수의 수행시간 출력
print('evaluate_n2의 수행시간:', end_n2-start_n2)
print('evaluate_n의 수행시간:', end_n-start_n)