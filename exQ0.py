



def fun1 (num1, num2):
    
    answer = 0
    if num1< num2:
        ranges = num1
    else:
        ranges = num2
        
    
    for i in range(ranges,0,-1):
            
        if num1%i == 0 and num2%i == 0:
            answer = i
            break
            
    return answer

num1 = int(input("정수입력 1.."))
num2 = int(input("정수입력 2.."))

print(f'최대공약수는 ... {fun1(num1,num2)}')