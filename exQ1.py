def fun2 (num1, num2):
    
    answer = 0
    if num1< num2:
        ranges = num1
    else:
        ranges = num2
        
    
    for i in range(ranges,0,-1):
            
        if num1%i == 0 and num2%i == 0:
            maxi = i
            break
        
    answer =  maxi* num1/maxi * num2/maxi    
        
            
    return answer



num1 = int(input("정수입력 1.."))
num2 = int(input("정수입력 2.."))

print(f'최소공배수는 ... {int(fun2(num1,num2))}')