

num = str(input("숫자 입력"))


for i in range (len(num)):
    
    if i == 0:
        sum = int( num[i])
        continue
    
    if int(num[i]) != 0 and sum != 0:
        sum = sum*int(num[i])
    else:
        sum = sum+int(num[i])
        
print(sum)



