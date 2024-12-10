# 일곱 난쟁이
arr = []
for i in range(9):
    arr.append(int(input()))
arr_sum = sum(arr)

def function():
    for i in range(8):
        for j in range(i+1,9):
            if arr_sum - (arr[i]+arr[j]) == 100:
                return [arr[i],arr[j]]


result = set(arr)-set(function())
result = sorted(list(result))
for x in result:
    print(x)