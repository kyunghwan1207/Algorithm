'''
def get_subsetsum(idx, sum_val):
    global ans
    if idx == n: return
    if sum_val + arr[idx] == s:
        ans += 1
    get_subsetsum(idx+1, sum_val + arr[idx])  # idx번째 원소를 부분수열에 포함시킨 경우
    get_subsetsum(idx+1, sum_val) # idx번째 원소를 부분수열에 포함시키지 않은 경우

if __name__ == "__main__":
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    get_subsetsum(0, 0)
    print(ans)
'''
def getSubSeqSum(numList, idx, sumVal, n, s):
    global cnt
    if idx >= len(numList):
        return
    if sumVal + numList[idx] == s:
        cnt += 1
    getSubSeqSum(numList, idx + 1, sumVal + numList[idx], n, s)
    getSubSeqSum(numList, idx + 1, sumVal, n, s)

if __name__ == "__main__":
    global cnt;
    n, s = map(int, input().split())
    numList = list(map(int, input().split()))
    cnt = 0
    getSubSeqSum(numList, 0, 0, n, s)
    print(cnt)
