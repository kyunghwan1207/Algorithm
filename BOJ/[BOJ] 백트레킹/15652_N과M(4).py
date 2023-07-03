def printNumSeq(n, m, start, s):
    if len(s) == m:
        # print(s)
        print(' '.join(map(str, s)))
        return
    for i in range(start,n+1):
        s.append(i)
        printNumSeq(n, m, i, s)
        s.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    s = []
    start = 1
    printNumSeq(n, m, start, s)