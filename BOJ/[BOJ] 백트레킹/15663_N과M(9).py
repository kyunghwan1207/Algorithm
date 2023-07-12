
def printSeqNum(seqList, numList, visited, m):
    if len(seqList) == m:
        print(*seqList)
        return
    prev = 0
    for i in range(0, len(numList)):
        if not visited[i] and prev != numList[i]:
            seqList.append(numList[i])
            visited[i] = True
            prev = numList[i]
            printSeqNum(seqList, numList, visited, m)
            seqList.pop()
            visited[i] = False

if __name__ == "__main__":
    n, m = map(int, input().split())
    numList = sorted(list(map(int, input().split())))
    visited = [False] * n
    seqList = []
    printSeqNum(seqList, numList, visited, m)

'''
동일 값은 append되어도 괜찮지만 자기 자신은 중복될 수 없기 때문에 visited[] 배열로 관리함.
numList는 '정렬'했기 때문에 바로 이전 값(prev)을 기억해서
numList[i]을 seqList[]에 넣을지 말지 if 조건으로 판별하여 중복된 수열을 여러번 출력하는 것을 막을 수 있다. 
'''