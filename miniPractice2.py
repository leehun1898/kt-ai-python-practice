
from multiprocessing.connection import answer_challenge
from unittest import result



    
roop = int(input('반복횟수를 입력하세요'))


shell = [None]*roop

for i in range(roop):
    val = int(input('정수를 를 입력하세요'))
    shell[roop-i-1] = val


for i in range (len(shell)):
    print(shell[i])