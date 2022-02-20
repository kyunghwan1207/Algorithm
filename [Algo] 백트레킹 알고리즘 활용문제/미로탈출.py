def find_way_from_maze(r, c): # 현재 칸 (r, c) 방문 중인 상태
	'''M을 문자열로 '0'(빈칸)/ '1'(장애물)로 받는다 '''
	visited[r][c] = True
	if r == ex and c == ey: return True
	# 현재칸 if safe?
	if M[r][c] == '0' or M[r][c] == 's':
		#if 동쪽 is safe and not visited[][]:
		if M[r][c+1] == '0' and not visited[r][c+1]:
			if find_way_from_maze(r, c+1):
				M[r][c+1] = trace # trace는 dot으로 탈출 경로를 표시하기 위함
				return True
		#if 남쪽 is safe and not visited[][]:
		if M[r+1][c] == '0' and not visited[r+1][c]:
			if find_way_from_maze(r+1, c):
				M[r+1][c] = trace # trace는 dot으로 탈출 경로를 표시하기 위함
				return True
		#if 서쪽 is safe and not visited[][]:
		if M[r][c-1] == '0' and not visited[r][c-1]:
			if find_way_from_maze(r, c-1):
				M[r][c-1] = trace
				return True
		if M[r-1][c] == '0' and not visited[r-1][c]:
			if find_way_from_maze(r-1, c):
				M[r-1][c] = trace
				return True
	else:
		return False
	
'''start of main'''
trace = '\u00B7'
n = int(input())
sx, sy, ex, ey = (int(x) for x in input().split())
M = []
# row 0 and n+1 are all 1's
# col 0 and n+1 are all 1's
for i in range(n):
	M.append([c for c in input()])

visited = [[False for _ in range(n)] for _ in range(n)]
M[sx][sy] = 's'
success = find_way_from_maze(sx, sy)
M[ex][ey] = 'e'

if success:
	for row in M:
		for c in row:
			if c == '1': 
				print('#', end="")
			elif c == '0':
				print(' ', end="")
			else:
				print(c, end="")
		print()
	print()
else:
	print("NO WAY!")
'''end of main'''
