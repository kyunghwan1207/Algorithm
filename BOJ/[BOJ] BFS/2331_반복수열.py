# 1630 -> 1715 성공1 (너무 어렵게 생각하지 말자, 왜냐하면 이미 같은 값이 한번 나온 순간 반복된 패턴이 나올 것임.)
import sys

def get_val(val, po):
    res = 0
    for v in str(val):
        res += int(v)**po
    return res

if __name__ == "__main__":
    input = sys.stdin.readline
    D = []
    A, p = map(int, input().split())
    D.append(A)
    idx = 0
    while True:
        val = get_val(D[-1], p)
        D.append(val)
        for i in range(len(D)):
            val = D[i]
            for j in range(i+1, len(D)):
                if val == D[j]:
                    print(i); exit(0)