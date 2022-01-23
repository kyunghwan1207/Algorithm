def two_sum(X, Y, t):
    '''
    X의 원소 i와 Y의 원소 j중 i + j == t인 i,j가 있는지 확인하고자 한다.

    for i in X로 돌면서
    key값으로 i - t값, value값으로 True를 저장하는 hash table을 만든다(수행시간: O(n))
    이후
    for j in Y로 돌면서
    hash table에 key값으로 -j값이 있는지 확인한다(수행시간: O(n))
    
    '''
    H = {i-t:True for i in X} # make hash table -> O(n)
    
    for j in Y:
        if H.get(-j): # find key which equal to -j in hash table -> O(n)
            return True # H[-j]
    return False

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

#for-else문 사용o, 리스트 원소접근법 사용o
for i in C:
    if two_sum(A, B, -i): # C의 원소를 하나씩 two_sum함수에 전달하면서 a+b+c=0을 만족하는 쌍이 있는지 확인 (수행시간: O(n))
        print(True)
        break
else: # for문이 interrupt없이 정상적으로 종료된다면 앞서언급한 a+b+c=0을 만족하는 쌍이 없는 것이므로 False를 출력한다.
    print(False)

'''
<수행시간 분석>
두 리스트의 각 원소의 합이 t와 같은지 여부를 판단하는 two_sum(X, Y, t)함수에 
리스트C의 원소를 하나씩 전달하면서 a+b+c=0을 만족하는 (a,b,c)가 존재하는지 확인한다.( 수행시간1: O(n) )

two_sum(X, Y, y)함수에서 전달된 두 개의 리스트인 X, Y를 통해서 
    X의 원소 i와 Y의 원소 j중 i + j == t인 (i,j)가 있는지 확인하고자 한다.

    for i in X로 리스트X의 원소를 하나씩 탐색하면서
    key값으로 i - t값, value값으로 True를 저장하는 hash table을 만든다( 수행시간1-1: O(n) )
    이후
    for j in Y로 리스트Y의 원소를 하나씩 탐색하면서
    hash table에 key값으로 -j값이 있는지 확인한다( (평균적인 경우)수행시간1-2: O(n) )
    => two_sum()함수에서의 총 수행시간은 "수행시간1-1 + 수행시간1-2" 이므로 O(cn) = O(n)이다.

앞서 리스트 C의 원소를 two_sum()함수로 하나씩 전달한다고 했으므로
=> 전체 알고리즘의 총 수행시간은 "수행시간1 * (수행시간1-1 + 수행시간1-2)"이므로 O(n*n) = O(n^2)이다.
'''