


def waterPay(company, useing):
    
    pay = 0
    
    if 'A' == company:
        pay = useing * 100
        
    elif useing <= 50: 
        pay =  useing*150 
    else: pay =  (useing-50)*150 

    return pay

company= input('회사 입력 :')
useing = input('사용양 입력 :')

print(f'수도요금은 {waterPay(company, useing)}')
    

    
    
    
  