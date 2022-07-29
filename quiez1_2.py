
num = int(input('반복횟수 입력..'))

for i in range(1, num +1 ):
    if i%2 :
        print("+", end="")
    else:
        print("-", end="")