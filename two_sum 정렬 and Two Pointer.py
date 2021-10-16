def two_sum(X, Y, t):
    '''정렬된 두 리스트에서 각자 X[0->n-1], Y[0<-n-1]로 다가가면서 두 원소의 합이 t가 되는 경우가 있는지 선형탐색한다.'''
    i, j = 0, len(Y)-1
    while i < len(X) and j >= 0:
        if X[i] + Y[j] == t:
            #찾은 값이 있다면 True를 return
            return True
        elif X[i] + Y[j] < t:
            #정렬된 두 리스트에서 각자 X[0->n-1], Y[0<-n-1]로 다가가고 있기때문에
            # 만약 두 원소의 합이 t보다 작다면 두 원소의 합의 크기를 증가시켜야 하므로 비교적 작은값을 가리키는 X의 인덱스인 i를 ++
            i += 1
        else:
            # 반대의 경우라면 두 원소의 합이 t보다 크기 때문에 두 원소의 합의 크기를 감소시켜야 하므로 비교적 큰값을 가리키는 Y의 인덱스인 j를 --
            j -= 1
    return False # 선형탐색을 모두 실시했지만 X[i] + Y[j] == t인 경우가 없다면 False를 return 
'''while을 통해서 i가 n-1까지 가거나 j가 0까지 갈 동안 아래의 조건문을 수행(무조건 매번 i나 j는 움직인다.)하므로 최악의 경우의 수행시간-> O(n)'''
#start of main
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

A.sort() #리스트 정렬 by Tim-sort algorithm-> O(nlogn)
B.sort() #리스트 정렬 by Tim-sort algorithm-> O(nlogn)

#for문을 다르게 사용해보자(for-else문 사용x, 리스트 인덱스 접근법 사용o)
triple = False
for i in range(len(C)): # C의 원소를 하나씩 two_sum함수에 전달하면서 a+b+c=0을 만족하는 쌍이 있는지 확인-> 수행시간1: O(n)
    if two_sum(A, B, -C[i]):
        triple = True
        break
print(True if triple else False)
'''
<수행시간 분석>
두 리스트를 정렬한다. 수행시간0: O(nlogn)
두 리스트의 각 원소의 합이 t와 같은지 여부를 판단하는 two_sum(X, Y, t)함수에 
리스트C의 원소를 하나씩 전달하면서 a+b+c=0을 만족하는 (a,b,c)가 존재하는지 확인한다.( 수행시간1: O(n) )

two_sum(X, Y, y)함수에서 전달된 두 개의 리스트인 X, Y를 통해서 
    정렬된 두 리스트에서 각자 X[0->n-1], Y[0<-n-1]로 다가가면서 두 원소의 합이 t가 되는 경우가 있는지 선형탐색한다.( (최악의 경우)수행시간2: O(n) )

앞서 두 리스트를 정렬하고(수행시간0) 리스트 C의 원소를 two_sum()함수로 하나씩 전달한다(수행시간1)고 했으므로
=> 전체 알고리즘의 총 수행시간은 "수행시간0 + 수행시간1 * 수행시간2"이므로 O(nlogn + n*n) = O(n^2)이다.

<해시 테이블 vs two-pointer>
two_sum함수에서 헤시테이블을 사용한 경우 "평균적인 시간"이 O(n)이지만
정렬을 통한 two-pointer방식은 "최악의 경우 시간"이 O(n)이므로 정렬을 통한 two-pointer방식이 더 좋은 알고리즘이라고 할 수 있다.
'''