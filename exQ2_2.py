# Q2 Answer template

def solution(numbers):
    answer = -1
    sum = 0
    for i in range(1, 10):
        if i not in numbers:
            sum += i
            
    if sum != 0:
        answer = sum
    return answer

numbers = [1,2,3,4,6,7,8,0]
answer = solution(numbers)
print(answer)