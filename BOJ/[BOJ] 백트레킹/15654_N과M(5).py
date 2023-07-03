def printNumSeq(m, lis, s):
    if len(s) == m:
        # print(s)
        print(' '.join(map(str, s)))
        return
    for e in lis:
        if e not in s:
            s.append(e)
            printNumSeq(m, lis, s)
            s.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    lis = sorted(list(map(int, input().split())))
    s = []
    printNumSeq(m, lis, s)
