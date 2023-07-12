def printSeqNum(numList, seqList, startIdx, m):
    if len(seqList) == m:
        print(' '.join(map(str, seqList)))
        return
    prev = 0
    for i in range(startIdx, len(numList)):
        if prev != numList[i]:
            seqList.append(numList[i])
            prev = numList[i]
            printSeqNum(numList, seqList, i, m)
            seqList.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    numList = sorted(list(map(int, input().split())))
    seqList = []
    startIdx = 0
    printSeqNum(numList, seqList, startIdx, m)