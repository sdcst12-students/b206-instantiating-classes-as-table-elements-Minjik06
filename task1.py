class team:
    wins = 0
    losses = 0
    games = 0
    results = {}

    def points(self):
        return 
    
    def record(self):
        return

    def win(self,w):
        self.wins+=w
        return 
    
    def loss(self,l):
        self.losses+=l
        return
    
    def __init__(self):
        pass


gameData = [{'t1': 'A', 's1': 2, 't2': 'B', 's2': 3}, {'t1': 'A', 's1': 4, 't2': 'C', 's2': 3}, {'t1': 'A', 's1': 1, 't2': 'D', 's2': 0}, {'t1': 'A', 's1': 0, 't2': 'E', 's2': 2}, {'t1': 'A', 's1': 4, 't2': 'F', 's2': 2}, {'t1': 'A', 's1': 2, 't2': 'G', 's2': 4}, {'t1': 'B', 's1': 2, 't2': 'A', 's2': 1}, {'t1': 'B', 's1': 2, 't2': 'C', 's2': 1}, {'t1': 'B', 's1': 3, 't2': 'D', 's2': 2}, {'t1': 'B', 's1': 3, 't2': 'E', 's2': 0}, {'t1': 'B', 's1': 3, 't2': 'F', 's2': 1}, {'t1': 'B', 's1': 2, 't2': 'G', 's2': 0}, {'t1': 'C', 's1': 0, 't2': 'A', 's2': 2}, {'t1': 'C', 's1': 0, 't2': 'B', 's2': 0}, {'t1': 'C', 's1': 3, 't2': 'D', 's2': 4}, {'t1': 'C', 's1': 1, 't2': 'E', 's2': 1}, {'t1': 'C', 's1': 3, 't2': 'F', 's2': 4}, {'t1': 'C', 's1': 3, 't2': 'G', 's2': 1}, {'t1': 'D', 's1': 1, 't2': 'A', 's2': 3}, {'t1': 'D', 's1': 2, 't2': 'B', 's2': 0}, {'t1': 'D', 's1': 4, 't2': 'C', 's2': 4}, {'t1': 'D', 's1': 2, 't2': 'E', 's2': 2}, {'t1': 'D', 's1': 3, 't2': 'F', 's2': 3}, {'t1': 'D', 's1': 2, 't2': 'G', 's2': 1}, {'t1': 'E', 's1': 2, 't2': 'A', 's2': 0}, {'t1': 'E', 's1': 4, 't2': 'B', 's2': 2}, {'t1': 'E', 's1': 0, 't2': 'C', 's2': 2}, {'t1': 'E', 's1': 3, 't2': 'D', 's2': 1}, {'t1': 'E', 's1': 0, 't2': 'F', 's2': 4}, {'t1': 'E', 's1': 2, 't2': 'G', 's2': 1}, {'t1': 'F', 's1': 2, 't2': 'A', 's2': 1}, {'t1': 'F', 's1': 3, 't2': 'B', 's2': 3}, {'t1': 'F', 's1': 1, 't2': 'C', 's2': 4}, {'t1': 'F', 's1': 0, 't2': 'D', 's2': 1}, {'t1': 'F', 's1': 0, 't2': 'E', 's2': 1}, {'t1': 'F', 's1': 2, 't2': 'G', 's2': 2}, {'t1': 'G', 's1': 4, 't2': 'A', 's2': 2}, {'t1': 'G', 's1': 0, 't2': 'B', 's2': 0}, {'t1': 'G', 's1': 1, 't2': 'C', 's2': 2}, {'t1': 'G', 's1': 0, 't2': 'D', 's2': 3}, {'t1': 'G', 's1': 4, 't2': 'E', 's2': 3}, {'t1': 'G', 's1': 3, 't2': 'F', 's2': 2}, {'t1': 'G', 's1': 2, 't2': 'F', 's2': 3}, {'t1': 'G', 's1': 2, 't2': 'E', 's2': 2}, {'t1': 'G', 's1': 4, 't2': 'D', 's2': 2}, {'t1': 'G', 's1': 3, 't2': 'C', 's2': 3}, {'t1': 'G', 's1': 0, 't2': 'B', 's2': 0}, {'t1': 'G', 's1': 0, 't2': 'A', 's2': 0}, {'t1': 'F', 's1': 1, 't2': 'G', 's2': 4}, {'t1': 'F', 's1': 2, 't2': 'E', 's2': 3}, {'t1': 'F', 's1': 1, 't2': 'D', 's2': 3}, {'t1': 'F', 's1': 0, 't2': 'C', 's2': 1}, {'t1': 'F', 's1': 4, 't2': 'B', 's2': 2}, {'t1': 'F', 's1': 4, 't2': 'A', 's2': 4}, {'t1': 'E', 's1': 4, 't2': 'G', 's2': 1}, {'t1': 'E', 's1': 3, 't2': 'F', 's2': 0}, {'t1': 'E', 's1': 0, 't2': 'D', 's2': 0}, {'t1': 'E', 's1': 0, 't2': 'C', 's2': 4}, {'t1': 'E', 's1': 3, 't2': 'B', 's2': 3}, {'t1': 'E', 's1': 4, 't2': 'A', 's2': 0}, {'t1': 'D', 's1': 0, 't2': 'G', 's2': 2}, {'t1': 'D', 's1': 3, 't2': 'F', 's2': 2}, {'t1': 'D', 's1': 2, 't2': 'E', 's2': 1}, {'t1': 'D', 's1': 3, 't2': 'C', 's2': 3}, {'t1': 'D', 's1': 4, 't2': 'B', 's2': 1}, {'t1': 'D', 's1': 3, 't2': 'A', 's2': 0}, {'t1': 'C', 's1': 2, 't2': 'G', 's2': 1}, {'t1': 'C', 's1': 1, 't2': 'F', 's2': 3}, {'t1': 'C', 's1': 4, 't2': 'E', 's2': 4}, {'t1': 'C', 's1': 4, 't2': 'D', 's2': 3}, {'t1': 'C', 's1': 1, 't2': 'B', 's2': 1}, {'t1': 'C', 's1': 3, 't2': 'A', 's2': 1}, {'t1': 'B', 's1': 3, 't2': 'G', 's2': 3}, {'t1': 'B', 's1': 3, 't2': 'F', 's2': 2}, {'t1': 'B', 's1': 3, 't2': 'E', 's2': 2}, {'t1': 'B', 's1': 3, 't2': 'D', 's2': 1}, {'t1': 'B', 's1': 4, 't2': 'C', 's2': 2}, {'t1': 'B', 's1': 0, 't2': 'A', 's2': 1}, {'t1': 'A', 's1': 2, 't2': 'G', 's2': 4}, {'t1': 'A', 's1': 1, 't2': 'F', 's2': 0}, {'t1': 'A', 's1': 4, 't2': 'E', 's2': 3}, {'t1': 'A', 's1': 4, 't2': 'D', 's2': 2}, {'t1': 'A', 's1': 1, 't2': 'C', 's2': 2}, {'t1': 'A', 's1': 4, 't2': 'B', 's2': 0}]
teamname=['Ants', 'Bears', 'Cougars', 'Doges', 'Elephants', 'Foxes', 'Giants']
#lengthg=len([d for d in gameData if isinstance(d, dict)])
teamData={}

for i in teamname:
    teamData[i]= team()
print(teamData)
print( teamData['Ants'].wins )


for i in range(len(gameData)):
    if gameData[i]['s1']>gameData[i]['s2']:
        if gameData[i]['t1']=='A':
            teamData['Ants'].win(gameData[i]['s1'])
            for j in teamname:
                if gameData[i]['t2']==j[0:1]:
                    teamData[j].loss(gameData[i]['s2'])
        elif gameData[i]['t1']=='B':
            teamData['Bears'].win(gameData[i]['s1'])
            for j in teamname:
                if gameData[i]['t2']==j[0:1]:
                    teamData[j].loss(gameData[i]['s2'])
        elif gameData[i]['t1']=='C':
            teamData['Cougars'].win(gameData[i]['s1'])
            for j in teamname:
                if gameData[i]['t2']==j[0:1]:
                    teamData[j].loss(gameData[i]['s2'])
        elif gameData[i]['t1']=='D':
            teamData['Doges'].win(gameData[i]['s1'])
            for j in teamname:
                if gameData[i]['t2']==j[0:1]:
                    teamData[j].loss(gameData[i]['s2'])
        elif gameData[i]['t1']=='E':
            teamData['Elephants'].win(gameData[i]['s1'])
            for j in teamname:
                if gameData[i]['t2']==j[0:1]:
                    teamData[j].loss(gameData[i]['s2'])
        elif gameData[i]['t1']=='F':
            teamData['Foxes'].win(gameData[i]['s1'])
            for j in teamname:
                if gameData[i]['t2']==j[0:1]:
                    teamData[j].loss(gameData[i]['s2'])
        elif gameData[i]['t1']=='G':
            teamData['Giants'].win(gameData[i]['s1'])
            for j in teamname:
                if gameData[i]['t2']==j[0:1]:
                    teamData[j].loss(gameData[i]['s2'])

    elif gameData[i]['s1']<gameData[i]['s2']:
        if gameData[i]['t2']=='A':
            teamData['Ants'].win(gameData[i]['s2'])
            for j in teamname:
                if gameData[i]['t1']==j[0:1]:
                    teamData[j].loss(gameData[i]['s1'])
        elif gameData[i]['t2']=='B':
            teamData['Bears'].win(gameData[i]['s2'])
            for j in teamname:
                if gameData[i]['t1']==j[0:1]:
                    teamData[j].loss(gameData[i]['s1'])
        elif gameData[i]['t2']=='C':
            teamData['Cougars'].win(gameData[i]['s2'])
            for j in teamname:
                if gameData[i]['t1']==j[0:1]:
                    teamData[j].loss(gameData[i]['s1'])
        elif gameData[i]['t2']=='D':
            teamData['Doges'].win(gameData[i]['s2'])
            for j in teamname:
                if gameData[i]['t1']==j[0:1]:
                    teamData[j].loss(gameData[i]['s1'])
        elif gameData[i]['t2']=='E':
            teamData['Elephants'].win(gameData[i]['s2'])
            for j in teamname:
                if gameData[i]['t1']==j[0:1]:
                    teamData[j].loss(gameData[i]['s1'])
        elif gameData[i]['t2']=='F':
            teamData['Foxes'].win(gameData[i]['s2'])
            for j in teamname:
                if gameData[i]['t1']==j[0:1]:
                    teamData[j].loss(gameData[i]['s1'])
        elif gameData[i]['t2']=='G':
            teamData['Giants'].win(gameData[i]['s2'])
            for j in teamname:
                if gameData[i]['t1']==j[0:1]:
                    teamData[j].loss(gameData[i]['s1'])
        
print( teamData['Ants'].wins )
print( teamData['Bears'].losses )



"""
for i in range(lengthg):
    for p in range(4):
        for j in gameData[p]:
            print (j)
#if gameData[i]['t1']=='A'
"""

"""for i in range(len(gameData)):
    if gameData[i]['s1']>gameData[i]['s2']:
        if gameData[i]['t1']=='A':
            teamData['Ants'].win(gameData[i]['s1'])
        elif gameData[i]['t1']=='B':
            teamData['Bears'].wins+=teamData['Bears'].win(gameData[i]['s1'])
        elif gameData[i]['t1']=='C':
            teamData['Cougars'].wins+=teamData['Cougars'].win(gameData[i]['s1'])
        elif gameData[i]['t1']=='D':
            teamData['doges'].wins+=teamData['Doges'].win(gameData[i]['s1'])
        elif gameData[i]['t1']=='E':
            teamData['Elephants'].wins+=teamData['Elephants'].win(gameData[i]['s1'])
        elif gameData[i]['t1']=='F':
            teamData['Foxes'].wins+=teamData['Foxes'].win(gameData[i]['s1'])
        elif gameData[i]['t1']=='G':
            teamData['Giants'].wins+=teamData['Giants'].win(gameData[i]['s1'])
print( teamData['Ants'].wins )"""



"""for i in range(len(gameData)):
    if gameData[i]['s1']>gameData[i]['s2']:
        if gameData[i]['t1']=='A':
            teamData['Ants'].win(gameData[i]['s1'])
        elif gameData[i]['t1']=='B':
            teamData['Bears'].win(gameData[i]['s1'])
        elif gameData[i]['t1']=='C':
            teamData['Cougars'].win(gameData[i]['s1'])
        elif gameData[i]['t1']=='D':
            teamData['Doges'].win(gameData[i]['s1'])
        elif gameData[i]['t1']=='E':
            teamData['Elephants'].win(gameData[i]['s1'])
        elif gameData[i]['t1']=='F':
            teamData['Foxes'].win(gameData[i]['s1'])
        elif gameData[i]['t1']=='G':
            teamData['Giants'].win(gameData[i]['s1'])
    elif gameData[i]['s1']<gameData[i]['s2']:
        if gameData[i]['t2']=='A':
            teamData['Ants'].win(gameData[i]['s2'])
        elif gameData[i]['t2']=='B':
            teamData['Bears'].win(gameData[i]['s2'])
        elif gameData[i]['t2']=='C':
            teamData['Cougars'].win(gameData[i]['s2'])
        elif gameData[i]['t2']=='D':
            teamData['Doges'].win(gameData[i]['s2'])
        elif gameData[i]['t2']=='E':
            teamData['Elephants'].win(gameData[i]['s2'])
        elif gameData[i]['t2']=='F':
            teamData['Foxes'].win(gameData[i]['s2'])
        elif gameData[i]['t2']=='G':
            teamData['Giants'].win(gameData[i]['s2'])"""