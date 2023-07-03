def printNumSeq(s, start, n, m):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n+1):
        s.append(i)
        printNumSeq(s, i+1, n, m)
        s.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    s = []
    printNumSeq(s, 1, n, m)