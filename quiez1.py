


kWh = int(input("전기사용량을 입력해주세요.."))

#def eletricPay(kWh):
pay = 0
    
if 100> kWh:
    pay = 410 + (kWh*60.7)
    
elif 200> kWh:
    pay = 910 + (100*60.7)+((kWh-100)*125.9)
    
else : 
    pay = 1600 + (100*60.7)+(100*125.9)+((kWh-200)*187.9)
    
paxpay = (pay + pay*0.1 + pay*0.037)
        
   # retrun = int(paxpay)
    

print(f'전기요금 ...{int(paxpay)}')
#print(f'전기요금 ...{eletricPay(kWh)}')