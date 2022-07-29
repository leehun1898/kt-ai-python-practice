

def mk_lt():
    flag = True
    lte = []

    while flag:
        
        val = input("리스트 입력값을 적용하세요")
        if val == "end":
            flag = False
            
        if val != "end":
            lte.append(val)

    return lte

def serching(lte , key):
    result = -1
    for i in range(len(lte)):
        if lte[i] == key:
            result = i
    
    if result == -1:
        result = "값이 없습니다."
    return (result)


def min_max(lte):
    
    min = lte[0]
    maxi = lte[0]
    
    for i in range(len(lte)):
        if min > lte[i]:
            min = lte[i]
        if maxi < lte[i]:
            maxi = lte[i]
    ser_min = serching(lte , min)
    ser_max = serching(lte , maxi)
    
    
    return (ser_min , ser_max)

print(min_max(mk_lt()))
