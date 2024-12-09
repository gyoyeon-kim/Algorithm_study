n = int(input())  
for i in range(1, n+1):   
    n_sum = sum((map(int, str(i))))  
    result = i + n_sum
    
    if result == n:
        print(i)
        break
    if i == n:  
        print(0)