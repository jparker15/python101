#Randomizer

import random

listOfNames =["Alpha","Beta","Gamma","Delta","Epsilon"]
newList = [] 

def Randomizer (nList):
    count = 0
    length =len(nList)
    while count < length:
        count += 1
        ranName = nList[random.randint(0, len(nList)-1)]
        print(f"Count:{count}")
        # print(f"In Order: {name}")
        # print(f"RANDOM:{ranName}")

        if not ranName in newList:
            newList.append(ranName)
            
        else:
            length+=1

    print(newList)


Randomizer(listOfNames)