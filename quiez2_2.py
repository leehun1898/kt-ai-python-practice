

from tkinter import W


flag = True
lte = []

while flag:
    
    val = input("리스트 입력값을 적용하세요")
    if val == "end":
        flag = False
        
    if val != "end":
        lte.append(val)

lte.sort(reverse=True)


for i in range(len(lte)):
    print(lte[i])