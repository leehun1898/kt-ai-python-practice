
result = []

for i in range(2, 1001):
    flag = True
    for j in range(2, i):
        if i % j ==0:
            flage = False
            break
    if flag :
        result.append(i)       
            
for k in range(len(result)):
    print(result[k])

