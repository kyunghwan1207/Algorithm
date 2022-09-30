def dfs(start):
    global ans, m
    if len(ans) == m:
        for a in ans:
            print(a, end =' ')
        print()
        return
    for i in range(start, n+1):
        if i not in ans:
            ans.append(i)
            dfs(i+1)
            ans.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    ans = []
    dfs(1)

'''
중복이 허용안되고 현재 인덱스위치 보다 큰 숫자만 ans에 넣어서 출력해야되기 때문에
dfs()함수로 모든 경우를 탐색할 때 넣을 원소의 시작 인덱스(start)를 함께 전달함
'''
