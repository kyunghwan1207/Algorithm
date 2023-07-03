def printNumSeq(s, n, m):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            printNumSeq(s, n, m)
            s.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    s = []
    printNumSeq(s, n, m)