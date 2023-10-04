import random

class NPC:
    stats = { 'str' : 0, 'int' : 0, 'pie' : 0, 'agi' : 0, 'stm' : 0, 'cha' : 0 }
    level = 0
    hp = 0
    gold = 0
    silver = 0
    copper = 0

    def __init__(self):
        return

stat = ['str', 'int', 'pie', 'agi', 'stm', 'cha']
print (NPC.stats)
for i in range(6):
    a=random.randint(1,6)
    b=random.randint(1,6)
    c=random.randint(1,6)
    NPC.stats[stat[i]]=round((a+b+c)/3)
print(NPC.stats)