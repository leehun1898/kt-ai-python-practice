
num = int(input('정수를 입력하시오...'))
flag = True

for i in range(1,num):
    for j in range(2,6):
        if i**j == num:
            print(i," ",j, end="")
            flag = False
        
if flag :
    print('결과없음')
        
            
             