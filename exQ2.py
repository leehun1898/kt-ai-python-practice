

num = int(input('0부터 99까지 숫자 입력'))

origin = num
count = 0

while True:
    
    if 10 > num:
        
        num = num*10 + num
        count += 1
        
    else :
        ten = int(num//10)
        one = int(num%10)
        sum = ten + one
        num = one*10 + sum
        count += 1
        
    if origin == num:
        break
    
print(f'반복횟수..{count}')
        