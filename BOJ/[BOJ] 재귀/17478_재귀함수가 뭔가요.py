import sys
input = sys.stdin.readline

def solution(x):
    global n
    print('____'*x , end = '' )
    print("\"재귀함수가 뭔가요?\"")
    print('____'*x, end = '')
    print("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
    print('____'*x, end = '')
    print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print('____'*x, end = '')
    print("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    if x == n-1: # n번째 재귀호출 시 출력할 챗봇멘트
        print('____'*(x+1) , end = '' )
        print("\"재귀함수가 뭔가요?\"")
        print('____'*(x+1) , end = '')
        print("\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print('____'*(x+1), end='')
        print("라고 답변하였지.")
        return
    elif x < n:
        solution(x+1)
        print('____'*(x+1), end='')
        print("라고 답변하였지.")
    
'''start of main'''
n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
solution(0)
print("라고 답변하였지.")
'''end of main'''

'''
<알고리즘 설명>
Step1. n을 입력받고 solution 함수에 인자값 0을 넣어서 호출
Step2. solution함수에서 전달받은 인자(x)를 문장앞에 쓰여지는 "____" 부분을 반복할 횟수로써 활용해서 문장 출력
Step3. x의 값에 따라서 재귀호출할지 함수를 return할지 조건문으로 판단

<수행시간 분석>
입력받은 수를 n이라고 하고, c는 상수라고 하면
Step1. O(c)
Step2. O(c)
Step3. O(c)
인데 Step2, 3은 x가 0 ~ n-1일 동안 반복되므로 solution함수 내에서 일어나는
Step2, 3의 수행시간은 O(c*n)이다.
=> 총 수행시간: O(n)
'''
