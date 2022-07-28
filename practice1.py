

a = int(input('1번째 :'))
b = int(input('2번째 :'))
c = int(input('3번째 :'))
d = int(input('4번째 :'))

maxi = a

if b > maxi:
    maxi = b
if c > maxi:
    maxi = c
if d > maxi:
    maxi = d
print(f"최대값은 -- {maxi}")