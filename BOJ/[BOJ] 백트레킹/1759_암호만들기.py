def isPossibleCode(caseList):
    global vowList
    vowCnt, conCnt = 0, 0
    for c in caseList:
        if c in vowList:
            vowCnt += 1
        else:
            conCnt += 1
    if vowCnt >= 1 and conCnt >= 2:
        return True
    return False

def printCode(caseList, seqList, startIdx, l):
    if len(seqList) == l and isPossibleCode(seqList):
        print(''.join(seqList))
        return

    for i in range(startIdx, len(caseList)):
        seqList.append(caseList[i])
        printCode(caseList, seqList, i+1, l)
        seqList.pop()

if __name__ == "__main__":
    l, c = map(int, input().split())
    caseList = sorted(list(map(str, input().split())))
    vowList = ['a', 'e', 'i', 'o', 'u'] # 모음
    # conList = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'] # 자음
    startIdx = 0
    seqList = []
    printCode(caseList, seqList, startIdx, l)
