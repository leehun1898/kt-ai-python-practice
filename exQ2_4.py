# Q4 Answer Template

def solution(arr):
    answer = 1
    arr.sort()
    num = 1
    result = []
    
    for i in range(arr[len(arr)-1],1,-1):
        for j in arr:
            if j % i == 0:
                num = i
    
    for i in arr:
        if i == num:
            result.append(i)
            continue
        result.append(i //num)
    
    for i in result:
        answer *= i
        
    
    
    return answer

arr = [2,6,8,14]
answer = solution(arr)
print(answer)