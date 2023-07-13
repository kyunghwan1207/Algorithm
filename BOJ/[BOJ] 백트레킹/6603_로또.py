def printAllCase(s, selectedList, startIdx):
    if len(selectedList) == 6:
        print(' '.join(map(str, selectedList)))
        return
    for i in range(startIdx, len(s)):
        selectedList.append(s[i])
        printAllCase(s, selectedList, i+1)
        selectedList.pop()


if __name__ == "__main__":
    while True:
        inputList = list(map(int, input().split()))
        if inputList[0] == 0:
            break
        k, s = inputList[0], inputList[1:]
        selectedList = []
        startIdx = 0
        printAllCase(s, selectedList, startIdx)
        print()
