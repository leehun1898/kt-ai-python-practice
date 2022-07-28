


def fun1(left, right):
    

    if left > right:
        left,right = right,left
    
    for i in range(left, right+1):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
                
        if count/2 ==0:
            sum = sum +  i
        else :
            sum = sum - i
                
            
    
    return sum 


left = int(input('정수입력 1..'))
rigth = int(input('정수입력 2..'))

print(fun1(left,rigth))