def printNumSeq(numList, seqList, n, m):
    if len(seqList) == m:
        # print(seqList)
        print(' '.join(map(str, seqList)))
        return
    for num in numList:
        seqList.append(num)
        printNumSeq(numList, seqList, n, m)
        seqList.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    numList = sorted(list(map(int, input().split())))
    seqList = []
    printNumSeq(numList, seqList, n, m)
