import datetime
import time
from typing import NewType
i =0
ListOfAbsolutes = []
n = 7

while(n > 0):
    print(n)
    n -= 1
    time.sleep(0.5)


#ListOfAbsolutes.append(miliseconds)


while i < 500:
    miliseconds = time.time()*1000
    print(str(i) + ":  " + str(miliseconds))
    i+= 1
    time.sleep(0.02)

# i = 1
# differens = []
# while i < len(ListOfAbsolutes):
#     differens.append(250 - (ListOfAbsolutes[i]-ListOfAbsolutes[i-1]))
#     i +=1

# diff = sum(differens)/len(differens)
# print(diff)


# n = 5
# while n > 0:
#     print(n)
#     n -=1
#     time.sleep(0.5)

# i = 0
# while i<200 :
#     print(datetime.datetime.now().time())
#     i += 1
#     time.sleep(0.24)

