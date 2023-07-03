def printNumSeq(n, m, s):
    if len(s) == m:
        # print(s)
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        s.append(i)
        printNumSeq(n, m, s)
        s.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    s = []
    printNumSeq(n, m, s)