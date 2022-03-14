import sys

piece = list(map(int, sys.stdin.readline().split()))

while(piece != [1, 2, 3, 4, 5]):
    for i in range(4):
        if piece[i] > piece[i+1]:
            piece[i], piece[i+1] = piece[i+1], piece[i]
            for j in range(5):
                if j != 4:
                    print(piece[j], end = ' ')
                else:
                    print(piece[j])