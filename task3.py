import random

class NPC:
    stats = { 'str' : 0, 'int' : 0, 'pie' : 0, 'agi' : 0, 'stm' : 0, 'cha' : 0 }
    level = 0
    hp = 0
    gold = 0
    silver = 0
    copper = 0
    wealth=0

    
    def __init__(self):
        return



npc={}
for i in range(100):
    npc[i]=NPC()
print(npc)


for i in range(100):
    #stat
    stat = ['str', 'int', 'pie', 'agi', 'stm', 'cha']
    print (NPC.stats)
    for i in range(6):
        a=random.randint(1,6)
        b=random.randint(1,6)
        c=random.randint(1,6)
        NPC.stats[stat[i]]=(a+b+c)
    print("STATS :",NPC.stats)


    #level
    lev=[1,1,1,1,2,2,2,3,3,4]
    NPC.level=random.choice(lev)
    print("LEVEL :", NPC.level)

    #hp
    for i in range(NPC.level):
        NPC.hp+=random.randint(1,10)
    print("HP :",NPC.hp)


    #gold
    goldp=[]
    for i in range(3):
        goldp.append(True)
    for j in range(7):
        goldp.append(False)

    if random.choice(goldp)==True:
        NPC.gold=random.randint(0,6)
    print("GOLD :",NPC.gold)


    #silver
    silverp=[True,False]
    if random.choice(silverp)==True:
        NPC.silver=random.randint(3,12)
    print("SILVER :",NPC.silver)


    #copper
    copperp=[True,True,True, False]
    if NPC.gold==0 and random.choice(copperp)==True:
            NPC.copper=random.randint(4,20)
    print("COPPER :",NPC.copper)


    #wealth
    if NPC.gold!=0:
        NPC.wealth=NPC.gold*100
    if NPC.silver!=0:
        NPC.wealth+=NPC.silver*10
    if NPC.copper!=0:
        NPC.wealth+=NPC.copper
    print("WEALTH :", NPC.wealth)





""" def wealth():
        w=0
        if self.gold!=0:
            w=self.gold*100
        if self.silver!=0:
            w+=self.gold*10
        if self.copper!=0:
            w+=self.copper
        return w"""




"""#stat
stat = ['str', 'int', 'pie', 'agi', 'stm', 'cha']
print (NPC.stats)
for i in range(6):
    a=random.randint(1,6)
    b=random.randint(1,6)
    c=random.randint(1,6)
    NPC.stats[stat[i]]=(a+b+c)
print("STATS :",NPC.stats)


#level
lev=[1,1,1,1,2,2,2,3,3,4]
NPC.level=random.choice(lev)
print("LEVEL :", NPC.level)

#hp
for i in range(NPC.level):
    NPC.hp+=random.randint(1,10)
print("HP :",NPC.hp)


#gold
goldp=[]
for i in range(3):
    goldp.append(True)
for j in range(7):
    goldp.append(False)

if random.choice(goldp)==True:
    NPC.gold=random.randint(0,6)
print("GOLD :",NPC.gold)


#silver
silverp=[True,False]
if random.choice(silverp)==True:
    NPC.silver=random.randint(3,12)
print("SILVER :",NPC.silver)


#copper
copperp=[True,True,True, False]
if NPC.gold==0 and random.choice(copperp)==True:
        NPC.copper=random.randint(4,20)
print("COPPER :",NPC.copper)


#wealth
if NPC.gold!=0:
    NPC.wealth=NPC.gold*100
if NPC.silver!=0:
    NPC.wealth+=NPC.silver*10
if NPC.copper!=0:
    NPC.wealth+=NPC.copper
print("WEALTH :", NPC.wealth)"""

"""import random

class NPC:
    stats = { 'str' : 0, 'int' : 0, 'pie' : 0, 'agi' : 0, 'stm' : 0, 'cha' : 0 }
    level = 0
    hp = 0
    gold = 0
    silver = 0
    copper = 0
    wealth=0

    
    def __init__(self):
        return
    
    def st(self):
        stat = ['str', 'int', 'pie', 'agi', 'stm', 'cha']
        for i in range(6):
            a=random.randint(1,6)
            b=random.randint(1,6)
            c=random.randint(1,6)
            self.stats[stat[i]]=(a+b+c)

    def le(self):
        lev=[1,1,1,1,2,2,2,3,3,4]
        self.level=random.choice(lev)

    def HP(self):
        for i in range(self.level):
            self.hp+=random.randint(1,10)

    def go(self):
        goldp=[]
        for i in range(3):
            goldp.append(True)
        for j in range(7):
            goldp.append(False)

        if random.choice(goldp)==True:
            self.gold=random.randint(0,6)

    def si(self):
        silverp=[True,False]
        if random.choice(silverp)==True:
            self.silver=random.randint(3,12)
    def co(self):
        copperp=[True,True,True, False]
        if self.gold==0 and random.choice(copperp)==True:
                self.copper=random.randint(4,20)
    def wel(self):
        if self.gold!=0:
            self.wealth=self.gold*100
        if self.silver!=0:
            self.wealth+=self.silver*10
        if self.copper!=0:
            self.wealth+=self.copper


npc={}
for i in range(100):
    npc[i]=NPC()
print(npc)


for i in range(100):
    #stat
    npc[i].st()

    #level
    npc[i].le()

    #hp
    npc[i].HP()


    #gold
    npc[i].go()


    #silver
    npc[i].si()


    #copper
    npc[i].co()


    #wealth
    npc[i].wel()"""