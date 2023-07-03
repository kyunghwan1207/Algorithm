def printNumSeq(m, start, lis, s):
    if len(s) == m:
        # print(s)
        print(' '.join(map(str, s)))
        return
    for i in range(start, len(lis)):
        s.append(lis[i])
        printNumSeq(m, i+1, lis, s)
        s.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    lis = sorted(list(map(int, input().split())))
    s = []
    printNumSeq(m, 0, lis, s)