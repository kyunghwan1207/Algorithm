import sys
input = sys.stdin.readline

'''
left child = 2i + 1
right child = 2i + 2
ord("A") = 65 ~ Z: 90
chr(65) = "A"
'''
def preorder(parent_idx, child_idx):
    global tree
    global preorder_result
    try:
        x = tree[parent_idx][child_idx]
    except IndexError :
        return
    if x == '.':
        return
    preorder_result += x # 현재노드 방문처리
    preorder(ord(x)-65, 1) # 왼쪽자식방문
    preorder(ord(x)-65, 2) # 오른쪽자식방문
    

def inorder(parent_idx, child_idx):
    global tree
    global inorder_result
    try:
        x = tree[parent_idx][child_idx]
    except IndexError :
        return
    if x == '.':
        return
    inorder(ord(x)-65, 1) # 왼쪽자식방문
    inorder_result += x # 현재노드 방문처리
    inorder(ord(x)-65, 2) # 오른쪽자식방문


def postorder(parent_idx, child_idx):
    global tree
    global postorder_result
    try:
        x = tree[parent_idx][child_idx]
    except IndexError :
        return
    if x == '.':
        return
    postorder(ord(x)-65, 1) # 왼쪽자식 방문
    postorder(ord(x)-65, 2) # 오른쪽자식 방문
    postorder_result += x # 현재노드 방문처리


'''start of main'''
n = int(input())
tree = list()
preorder_result = ''
inorder_result = ''
postorder_result = ''
for _ in range(n):
    tree.append(input().split())
tree.sort(key = lambda x: x[0])  # tree리스트의 각 원소x의 x[0]을 기준으로 오름차순정렬 -> O(nlogn)

preorder(0, 0)
print(preorder_result)
inorder(0, 0)
print(inorder_result)
postorder(0, 0)
print(postorder_result)
'''end of main'''

'''
<알고리즘 설명>
Stack 자료구조를 사용하는 것과 동일하게 재귀 알고리즘을 통해 트리를 순회합니다.
Step1. tree리스트에 원소입력받음
이때 알파벳이 A, B, C, D... 와 같이 순차적으로 입력되는 것이 아닙니다.
Step2. 알파벳 순으로 정렬
따라서 트리 순회 시 노드를 특정순서대로(부모방문 후 왼쪽자식 방문 or 부모방문 후 오른쪽자식 방문) 방문하기 편하게 하기 위해 알파벳기준 오름차순으로 정렬하였습니다.
Step3. 각 함수 내부 로직구현
그리고 tree리스트 원소 x의 x[0]는 부모, x[1]은 왼쪽자식, x[2]는 오른쪽자식이기 때문에
재귀함수 호출시 각 함수의 특성에 맞게 호출 순서를 조정했습니다.
전역변수(Global Variable)을 활용해서 함수호출을 반복하더라도 최종답이 유지되도록 하였고,
'.'이 인덱스 변환시 ord()함수에 인자로 넘어갈 경우를 대비해서 try except 문으로 IndexError가 발생할 경우 함수를 return시킴으로써 해결했습니다.

<수행시간 분석>
Step1. O(n)
Step2. O(nlogn) (이유: Python은 내부적으로 정렬시 Tim sort방식을 활용하기 때문)
Step3. 각 함수별로 O(n) 소요됨 (이유: 각 함수가 한번씩 수행될때 O(c)이지만 총 n개의 노드를 방문처리해야하기 때문)
=> 총 수행시간: O(n) + O(nlogn) + 3*O(n) = O(nlogn)
'''
