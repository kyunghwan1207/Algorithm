def getCopy(eggList):
    temp = []
    for s, w in eggList:
        temp.append([s, w])
    return temp
def getCntOfBreakedEgg(idx, eggList):
    global ans, n
    if idx == n:
        cnt = 0
        # print(eggList)
        for s, w in eggList:
            if s <= 0:
                cnt += 1
        ans = cnt if ans < cnt else ans
        return
    if eggList[idx][0] > 0:
        isHit = False
        for i in range(n):
            if eggList[i][0] > 0 and idx != i:
                isHit = True
                temp = getCopy(eggList)
                temp[i][0] -= temp[idx][1]
                temp[idx][0] -= temp[i][1]
                getCntOfBreakedEgg(idx+1, temp)
        if not isHit:
            getCntOfBreakedEgg(idx+1, eggList)
    else:
        getCntOfBreakedEgg(idx+1, eggList)


if __name__ == "__main__":
    n = int(input())
    eggList = [] # [[내구도, 무게], ...]
    for _ in range(n):
        eggList.append(list(map(int, input().split())))
    # print("eggList: ", eggList)
    ans = 0
    getCntOfBreakedEgg(0, eggList)
    print(ans)

'''
*1, 값이 이상하게 튈 때엔 (마이너스 값이 크게 나올 경우) 값 복사를 안전하게 했는지
(값 변경이 전역적으로 영향을 미치진 않는지 -> 리스트이 경우 ref를 복사하기 때문에 전역적으로 영향 미칠 수 있음!)
따라서 완전히 다른 리스트로 관리할 수 있도록 값을 복사하는 과정을 거쳐야함 -> temp = eggList[:]
2. 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 '하나'를 치는 것이기 때문에
맨 첫번째 계란은 고정으로 두고 나머지 계란을 치는경우, 안치는 경우로 나눠서 BT해보자!
3. 맨 마지막 계란도 hit은 하긴해야하기 때문에 함수 종료조건을 if idx == n:으로 두었다
'''