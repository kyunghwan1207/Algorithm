def printSeqNum(numList, seqList, m):
    if len(seqList) == m:
        print(' '.join(map(str, seqList)))
        return
    prev = 0
    for i in range(len(numList)):
        if prev != numList[i]:
            prev = numList[i]
            seqList.append(numList[i])
            printSeqNum(numList, seqList, m)
            seqList.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    numList = sorted(list(map(int, input().split())))
    seqList = []
    printSeqNum(numList, seqList, m)