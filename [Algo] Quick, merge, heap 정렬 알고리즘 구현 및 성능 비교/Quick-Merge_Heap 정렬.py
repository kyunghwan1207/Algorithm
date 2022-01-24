import random, timeit

##
## 여기에 세 가지 정렬함수를 위한 코드를...
##
def insertion_sort_forMerge(A, n):
    global Mc
    global Ms
    for i in range(1, n):
        j = i - 1
        Mc += 1
        while j >= 0 and A[j] > A[j+1]:
            Mc += 1
            Ms += 1
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1
    return A
def insertion_sort_forQuick(A, n):
    global Qc
    global Qs
    for i in range(1, n):
        j = i - 1
        Qc += 1
        while j >= 0 and A[j] > A[j+1]:
            Qc += 1
            Qs += 1
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1
    return A
def quick_sort(A, first, last):
    if first >= last: return
    left, right = first+1, last
    p = A[first]
    global Qc
    global Qs
    while left <= right:
        Qc += 1
        while left <= last and A[left] < p:
            Qc += 1
            left += 1
        Qc += 1
        while right > first and A[right] > p:
            Qc += 1
            right -= 1
        if left <= right:
            Qs += 1
            A[right], A[left] = A[left], A[right]
            left += 1
            right -= 1
    Qs += 1
    A[first], A[right] = A[right], A[first]
    k = 32
    max_length = -1
    left_length, right_length = right-first, last-left+1
    if left_length < right_length:
        max_length = right_length
    else: 
        max_length = left_length
    if max_length <= k:
        Qs += left_length
        A[first:right] = insertion_sort_forQuick(A[first:right], left_length)
        Qs += right_length
        A[left:last+1] = insertion_sort_forQuick(A[left:last+1], right_length)
    else:
        quick_sort(A, first, right-1)
        quick_sort(A, left, last)
    # quick_sort(A, first, right-1)
    # quick_sort(A, left, last)

def merge_sort(A, first, last):
    if first >= last: return
    m = (first + last) // 2
    k = 32
    global Mc
    global Ms
    max_length = -1
    left_length, right_length = m-first+1, last-m
    if left_length < right_length: 
        max_length = right_length
    else: 
        max_length = left_length
    if max_length <= k:
        Ms += left_length
        A[first:m+1] = insertion_sort_forMerge(A[first:m+1], left_length)
        Ms += right_length
        A[m+1:last+1] = insertion_sort_forMerge(A[m+1:last+1], right_length)
    else:
        merge_sort(A, first, m)
        merge_sort(A, m+1, last)
    # merge_sort(A, first, m)
    # merge_sort(A, m+1, last)
    # 각각 정렬된 두 개의 리스트 생김
    # 이 두 리스트를 merge해보자
    B = []
    i, j = first, m+1
    while i <= m and j <= last:
        Mc += 1
        if A[i] <= A[j]:
            Ms += 1
            B.append(A[i])
            i += 1
        else:
            Ms += 1
            B.append(A[j])
            j += 1
    for k in range(i, m+1):
        Ms += 1
        B.append(A[k])
    for k in range(j, last+1):
        Ms += 1
        B.append(A[k])
    for k in range(first, last+1):
        Ms += 1
        A[k] = B[k-first]
        
def make_heap(A):
    '''A를 max heap으로 만든다.'''
    n = len(A)
    for k in range(n//2 -1, -1, -1):
        heapify_down(A, k, n)
    
def heapify_down(A, k, n):
    '''
    n = 힙의 전체 노드 수[heap sort를 위해 필요] 
    A[k]가 힙성질을 위배한다면, 밑으로 내려가면서 힙성질을 만족하는 위치를 찾는다.
    '''
    global Hc
    global Hs
    while 2*k+1 < n:
        m = k
        L, R = 2*k+1, 2*k+2
        Hc += 1
        if L < n and A[L] > A[m]:
            m = L
        Hc += 1
        if R < n and A[R] > A[m]:
            m = R
        if m != k:
            Hs += 1
            A[m], A[k] = A[k], A[m]
            k = m
        else:
            break
def heap_sort(A):
    n = len(A)
    make_heap(A)
    global Hs
    for k in range(n - 1, 0, -1):
        Hs += 1
        A[0], A[k] = A[k], A[0]
        n = n-1
        heapify_down(A, 0, n)

# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))