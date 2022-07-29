# Q7 Answer Template

def solution(arr):
    answer = []
    prim = arr[0]
    answer.append(prim)
    for i in range(1, len(arr)):
        
        if arr[i] != prim:
            answer.append(arr[i])
            prim = arr[i]
       
    return answer

arr = [1,1,3,3,0,1,1]
#arr = [4,4,4,3,3]
answer = solution(arr)
print(answer)