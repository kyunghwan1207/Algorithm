def solve(A):
    n = len(A)
    left, right = [0]*n, [0]*n
    stack1, stack2 = [], [] #[value, index]형태의 원소가 저장되어서 이차원리스트로 활용됨
    count = 1 # 해당원소가 최솟값인 sub리스트의 개수(각 원소는 적어도 자기자신 하나만을 원소로 하는 sub리스트 하나정도는 꼭 가지고 있기 때문에 최소1 이상일 것임)
    for i in range(n):
        count = 1
        while len(stack1) > 0 and stack1[-1][0] > A[i]:#stack1이라는 리스트안에 원소가 리스트형태로 저장되므로 이차원리스트처럼 접근하면 됨.
            # 따라서 stack1의 peek역할을 stack1[-1]으로하고 해당 원소(stack1의 내부리스트)의 첫번째 원소(인덱스 0번=stack1[-1][0])에 최솟값이 저장되어있음.
            # stack1의 내부의 value은 오름차순으로 정렬된 형태를 유지.
            # stack1의 상단에 있는 값(stack1[-1][0])보다 더 작은 원소(A[i])가 등장한다면 이제 그 뒤부터 오는 sub리스트에는 A[i]가 최솟값이 되므로 A[i]의 count를 stack내부에있는 기존 count만큼 증가시킨 카운트를 저장 후
            # stack1의 내부의 value는 오름차순을 유지해야하므로 A[i]의 올바른 위치를 찾도록 pop수행.
            count += stack1[-1][1]
            stack1.pop()
        stack1.append([A[i], count])
        left[i] = count # A[i]가 최솟값이면서 A[i]로 끝나는 sub리스트의 개수
    for j in range(n-1, -1, -1):
        count = 1
        while len(stack2) > 0 and stack2[-1][0] > A[j]:
            # stack2의 내부 value는 오름차순으로 정렬된 상태를 유지하는 것은 동일하지만
            # 탐색순서를 stack1과 반대로 진행.
            count += stack2[-1][1]
            stack2.pop()
        stack2.append([A[j], count])
        right[j] = count # A[i]가 최솟값이면서 A[i]로 시작하는 sub리스트의 개수
    result = 0
    for k in range(n):
        result += A[k]*left[k]*right[k] #A[i]가 최솟값인 sub리스트의 개수가 겹치는 경우도 있기 때문에 곱셈으로 처리
    return result

'''start of main'''
A = [int(x) for x in input().split()]
print(solve(A))
'''end of main'''

'''
<알고리즘 설명>
큰 문제를 작은 문제로 생각하면
큰 문제는 모든 m(i, j)(0<=i<=j<=n)의 합을 구하는 것이기 때문에 
작은 문제로 각 sub리스트 하나하나에서 최솟값을 구해서 더해가면 됩니다.
ex) A = [1 2 -1 4]일때 sub리스트는 {[1], [2], [-1], [4], [1, 2], [2, -1], [-1, 4], [1, 2, -1], [2, -1, 4], [1, 2, -1, 4]}가 되고
각 sub리스트의 최솟값의 합은 (1+2-1+4) + (1-1-1) + (-1-1) + (-1) = 2 가 됩니다.
하지만 좀 더 효율적인 경우로 보면 위에 작성한 알고리즘처럼 "A[i]가 최솟값인 sub리스트의 개수(k[i])를 구할 수 있다"면 더 빠르게 계산할 수 있습니다.
따라서 "A[i]*k[i]의 모든 합"이 결국 최종해가 되는 것을 알 수 있습니다.
k[i]를 구할때 즉, A[i]가 최솟값인 sub리스트의 개수를 구해야할때 이중반복을 사용하지 않기 위해선
A[i]가 포함된 sub리스트 중 A[i]로 끝나는 sub리스트의 개수(left에 저장됨)와 A[i]로 시작하는 sub리스트의 개수를(right에 저장됨)각각 나눠서 구해야합니다.
1차원 dp테이블에 해당하는 left, right를 다 채우고나서 최종해를 구할때
이때 A[i] 원소 하나만 있는 경우와 같이 중복되기 때문에 k[i] = left[i]*right[i]로 계산합니다.

<수행시간 분석>
길이가 n인 리스트 A를 입력받음 -> O(n)
for반복문을 통해 n번 반복하면서 stack을 조정하고 left를 채웁니다.
stack을 조정하는 while문이 제일 많이 반복되는 최악의 경우는 A의 원소가 계속 오름차순으로 입력되다가 맨 마지막 원소가 최솟값일 경우인대
이때 기존에 오름차순으로 입력될 때는 while문이 수행되지 않다가 맨 마지막원소가 들어올때만 while이 n번 반복되기때문에
for문이 n번 반복될 동안 상수번의 연산이 이루어지다가 맨 마지막에 한번만 n번의 연산이 추가적으로 되므로 -> O(c*n) 입니다.
이후에 오는 stack을 조정하고 right를 채우는 반복문에서도 위와 유사하게 동작하기 때문에 -> O(c*n)입니다.
맨 마지막에 최종해를 구하는 연산 -> O(c*n)
=> 총 알고리즘의 수행시간 = O(n)
'''