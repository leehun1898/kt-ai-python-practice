
def mk_lt():
    flag = True
    lte = []

    while flag:
        
        val = input("리스트 입력값을 적용하세요")
        if val == "end":
            flag = False
            
        if val != "end":
            lte.append(val)

    #lte.sort(reverse=True)

    '''for i in range(len(lte)):
        print(lte[i])'''
    return lte

def serching(lte , key):
    result = -1
    for i in range(len(lte)):
        if lte[i] == key:
            result = i+1
    
    if result == -1:
        result = "값이 없습니다."
    return (result)


lte = mk_lt()
key = input("찾고자하는 값을 입력하시오..")
print(f"{serching(lte , key)}")