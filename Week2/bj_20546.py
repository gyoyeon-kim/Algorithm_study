Money = int(input())                               
MachineDuck = list(map(int, input().split()))    
   
# 준현
money_bnp = Money   
count_bnp = 0

# 성민
money_timing = Money
count_timing = 0

for num, price in enumerate(MachineDuck):

    # 준현
    count_bnp += (money_bnp // price)
    money_bnp %= price

    # 성민
    temp = MachineDuck[num:num+4]

    if len(temp) < 4:
        continue

    if temp[0] < temp[1] < temp[2] < temp[3] and count_timing > 0:         
        money_timing += (count_timing * temp[3])
        count_timing = 0
    elif temp[0] > temp[1] > temp[2] > temp[3]:                             
        count_timing += (money_timing // temp[3])
        money_timing %= temp[3]

answer_bnp = money_bnp + count_bnp * MachineDuck[-1]
answer_timing = money_timing + count_timing * MachineDuck[-1] 

if answer_bnp < answer_timing:
    print("TIMING")
elif answer_bnp > answer_timing:
    print("BNP")
else:
    print("SAMESAME")