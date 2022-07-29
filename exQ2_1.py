


def solution(lottos, win_nums):
    count = 0
    unkwn = 0
    answer = []
    for i in lottos:
        if i == 0:
            unkwn += 1
        for j in win_nums:
            if i == j :
                count += 1
    
    machNum = count + unkwn
    
    if machNum == 6:
        answer.append(1)
    elif machNum == 5:
        answer.append(2)
    elif machNum == 4:
        answer.append(3)
    elif machNum == 3:
        answer.append(4)
    elif machNum == 2:
        answer.append(5)
    elif machNum < 2:
        answer.append(6)
        
        
    if count == 6:
        answer.append(1)
    elif count == 5:
        answer.append(2)
    elif count == 4:
        answer.append(3)
    elif count == 3:
        answer.append(4)
    elif count == 2:
        answer.append(5)
    elif count < 2:
        answer.append(6)
        
    
    return answer



lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)