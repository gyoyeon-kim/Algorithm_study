board = []
n, m = map(int, input().split())

for i in range(n):
    board.append(list(map(int, input())))

def find(b, length):
    for i in range(0, n-length+1):
        for j in range(0, m-length+1):
            if b[i][j] == b[i+length-1][j] and b[i+length-1][j] == b[i][j+length-1] and b[i][j+length-1] == b[i+length-1][j+length-1]:
                return True
    
    return False

def result():
    size = min(n, m) #구할 수 있는 제일 큰 정사각형
    answer = 1
    
    for value in range(size, 0, -1):
        if find(board, value) == True:
            answer = value * value
            break
    
    print(answer)
    
result()