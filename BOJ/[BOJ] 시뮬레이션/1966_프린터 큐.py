import sys, math
input = sys.stdin.readline

# 현재 문서보다 높은 중요도를 가진 문서가 있/없다면 -> T/F
def check(p):
    global pl
    for i in range(p+1, 10):
        if pl[i] != 0:
            return True
    return False

'''start of main'''
tc = int(input())
for _ in range(tc):
    pl = [0]*10 # 중요도 1~9까지 각 인덱스에 저장
    cnt = 0 # 문서가 인쇄되는 순서
    # print(sys.maxsize) # 9223372036854775807
    n, m = map(int, input().split()) # 문서의 개수, 궁금한 문서의 위치
    # 포인터(idx)로 가르키면서 리스트를 원형큐 처럼 구현
    # 매번 리스트를 다 탐색하지말고 중요도 리스트(pl) 만들어서
    # 인덱스(=중요도) 별로 몇개의 수가 있는지 저장한다음
    # 현재 문서를 찾을때 현재 문서의 중요도 보다 높은 문서가 있다는 것을
    # pl에서 검사하자 -> O(9), 이후 잇다면 포인터만 ++해서 반복
    
    # 중요도 입력
    doc = list(map(int, input().split()))
    for i in range(n):
        pl[doc[i]] += 1
    idx = 0
    while True: # 2147000000
        if doc[idx] != -math.inf and not check(doc[idx]): # 현재문서보다 중요도가 높은 문서가 없다면
            if idx == m: # 출력할 문서라면
                cnt += 1
                print(cnt)
                break
            else:
                cnt+=1
                pl[doc[idx]] -= 1
                doc[idx] = -math.inf # 출력한 문서 체크

        #elif doc[idx] != -math.inf and check(idx): # 현재문서보다 중요도가 높은 문서가 있다면
        idx += 1
        if idx >= n:
            idx = 0
'''end of main'''

'''
<알고리즘 설명>
Step0. 사용할 변수, 리스트 초기화 
Step1. 중요도 리스트(pl)에 중요도(=인덱스)에 해당하는 문서의 개수를 해당 인덱스에 저장
Step2. 현재 문서의 중요도보다 더 높은 중요도를 가진 문서가 존재하는지 확인
Step3. 출력할 문서인지, 아닌지에 따라 적절하게 로직 수행
    
<수행시간 분석>
문서의 개수를 n, 테스트 케이스를 t, 상수를 c라고 하면
Step0. O(c+n)
Step1. O(n)
Step2,3. O(c)
여기서 
Step2,3은 최악의 경우 n만큼 반복되므로 O(c*n) = O(n)이고
Step0,1,2,3은 t만큼 반복되므로
=> 총 수행시간: O(t*c*n) = O(t*n)
'''
