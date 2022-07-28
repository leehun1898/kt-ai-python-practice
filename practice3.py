

a = int(input('정수입력..'))
b = int(input('정수입력..'))

if a > b:
    b,a = a,b 

sum = 0
for i in range(a, b):
    sum += i

    if i < b:
        print(f'{i} + ', end = "") 

print(f'{b}  = ', end = "")  
print(f'{sum}')
    
    