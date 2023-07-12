def printNumSeq(numList, seqList, startIdx, m):
    if len(seqList) == m:
        print(' '.join(map(str, seqList)))
        return
    for i in range(startIdx, len(numList)):
        seqList.append(numList[i])
        printNumSeq(numList, seqList, i, m)
        seqList.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    numList = sorted(list(map(int, input().split())))
    seqList = []
    startIdx = 0
    printNumSeq(numList, seqList, startIdx, m)