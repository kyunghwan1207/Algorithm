def can_place(r, c):
    for i in range(r):
        if row[i] == c or abs(i - r) == abs(row[i] - row[r]):
            return False
    return True

# k번째 행에 퀸 놓기
def place_queen(k):
    global answer, row
    if k == n:
        answer += 1
        return
    for j in range(n):
        row[k] = j  # k번째 행, j번째 열에 퀸을 놓음
        if can_place(k, j): # j 번째 열에 놓을 수 있는지 확인
            place_queen(k+1)

if __name__ == "__main__":
    n = int(input())
    answer = 0
    row = [0] * n
    place_queen(0)
    print(answer)
