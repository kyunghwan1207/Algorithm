def solution(brown, yellow):
    answer = []
    half_brown = brown//2
    for w in range(1, half_brown):
        for h in range(1, half_brown):
            if w+h != half_brown: continue
            if w < h+2: continue
            if (w-2)*h == yellow:
                answer = [w, h+2]   
                return answer
    return answer
'''
w >= h+2 이면서,
(w-2)*h = yellow 가 되는 w, h를 찾자
'''
