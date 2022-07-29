

a = [2,5,1,3,9,6,7]

def line_serch(a):
    
    key = 7
    i= 0
    count = 0
    while True :
        if a[i] == key:
            break
        if i == len(a):
            break
        i += 1
        count += 1
    return count

def senti_serch(a):
    
    key = 7
    b = a.copy()
    b.append(key)
    i = 0
    count =0; 
    
    while True:
        if b[i] == key:
            break
        i += 1
    
    if i == len(b): 
        count += 1
        return count 
    else: 
        count += 1
        return count 
    
    
print(f"선형 결과 .. {line_serch(a)}")
print(f"보초 결과 .. {senti_serch(a)}")
    
