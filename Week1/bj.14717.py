import sys
input = sys.stdin.readline

a, b = map(int, input().split())
total = 153 # 카드 2장을 제외하고 뽑을 수 있는 전체 카드 조합 >> 18 * 17
answer = 0

if a == b:
    answer = total - (10-a)
else:
    ypoint = (a+b) % 10
    for i in range(1, 11):
        for j in range(i+1, 11):
            if ypoint > (i+j) % 10:
                if i == a and j == b:
                    continue
                elif i == a or j == a or i == b or j == b:
                    answer += 2
                else:
                    answer += 4

print("%.3f" % (answer / total))
