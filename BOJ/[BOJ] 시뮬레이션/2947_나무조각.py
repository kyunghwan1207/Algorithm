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
'''
<알고리즘 설명>
Step1. 각 조각의 수를 접근해서 크기를 비교하기 위해 int형 원소로 리스트(piece)에 입력받음
Step2. piece리스트가 [1, 2, 3, 4, 5]가 아닌동안 반복문을 통해 문제에서 제시된 조각위치변경 과정을 거치면서 그때마다 조각의 순서를 출력함

<수행시간 분석>
Step1. O(c) (c는 상수)
Step2. O(4*5) = O(c)
=> 총 수행시간: O(c) + O(c) = O(c)
'''
