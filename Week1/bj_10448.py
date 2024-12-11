T = int(input())

tri = [i * (i+1) // 2 for i in range(1,45)] # 45번째 삼각수 == 1035

answer = [0] * 1001

for i in tri:
    for j in tri:
        for k in tri:
            if i + j + k <= 1000: # 3개의 수 합으로 1000아래의 값으로 만들 수 있으면 1
                answer[i+j+k] = 1

for _ in range(T):
    print(answer[int(input())])                
