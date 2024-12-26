n = int(input())
 
graph =  [] #아파트 호수를 입력받을 배열 
for _ in range(n):
  graph.append(list(map(int,input())))
 
visited = [[0]*n for _ in range(n)] #아파트 호수와 같은 방문 그래프
 
dx  = [-1,0,1,0] # x,y이동 좌표
dy = [0,1,0,-1]
 
def dfs(x,y,c):
  visited[x][y] = 1 # 방문 표시
  global nums # 아파트를 세기 위한 변수
  if graph[x][y] == 1:
    nums += 1
  for i in range(4): # 4방향으로 반목문을 통한 좌표 이동
    nx = x+dx[i]
    ny = y+dy[i]
    if 0<= nx < n and 0<= ny < n: # 벽을 넘지 않을때
      if visited[nx][ny] == 0 and graph[nx][ny] == 1: 
        #방문하지 않았고 , 호수가 1이라면 
        dfs(nx,ny,c) # 재귀적으로 dfs를 수행
 
cnt = 1 # 아파트 단지를 세기 위한 변수
numlist = [] #총 단지수를 담기 위한 배열
nums = 0 # 총 단지수
for a in range(n):
  for b in range(n):
    if graph[a][b] == 1 and visited[a][b] == 0 :
      dfs(a,b,cnt)
      numlist.append(nums)
      nums = 0 # 총 단지수를 담았다면 0으로 초기화
print(len(numlist)) # 총 단지수의 크기
for i in sorted(numlist): # 오름차순 정렬로 출력
  print(i)