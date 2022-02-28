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