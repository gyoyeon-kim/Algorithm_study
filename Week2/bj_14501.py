N = int(input())
timeTable = [list(map(int, input().split())) for _ in range(N)]

def get(i):
    if i>=N:
        return 0
    ret = 0
    if i+timeTable[i][0]<=N :
        ret = get(i+timeTable[i][0])+timeTable[i][1]
    ret = max(ret,get(i+1))
    return ret

print(get(0))