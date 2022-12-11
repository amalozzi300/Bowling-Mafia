import bowler as b
import team as t
import random
import math

def MyRandom(numBowl):
    return math.floor(random.random() * numBowl)

def InTeamList(newTeam, teamList):
    for i in range (len(teamList)):
        if newTeam == teamList[i]:
            return True

    return False

bowlers = []
teams = []
used = []

b1 = b.Bowler('1')
b2 = b.Bowler('2')
bowler1 = b1
bowler2 = b2

allUsed = False

f = open('mdBowlers.txt', 'r')
numBowlers = int(f.readline())
for i in range(numBowlers):
    name = f.readline()
    hdcp = int(f.readline())

    bowlers.append(b.Bowler(name, hdcp))
    used.append(False)

while (not allUsed):
    allUsed = True

    if bowler2 != b2:
        bowler1 = b1
    if bowler1 == b1:
        bowler2 = b2

    randNum = MyRandom(numBowlers)

    if not used[randNum]:
        if bowler1 == b1:
            bowler1 = bowlers[randNum]
            used[randNum] = True
        else:
            if bowler1 != bowlers[randNum]:
                bowler2 = bowlers[randNum]

    if bowler2 != b2:
        if len(teams) == 0:
            teams.append(t.Team(bowler1, bowler2))
            used[randNum] = True
        else:
            if not InTeamList(t.Team(bowler1, bowler2), teams):
                teams.append(t.Team(bowler1, bowler2))
                used[randNum] = True
            else:
                bowler2 = b2

    for i in range(numBowlers):
        if not used[i]:
            allUsed = False

f = open('mdTeams.txt', 'w')
f.write(str(int(numBowlers/2)) + '\n')
for i in range(len(teams)):
    f.write(teams[i].PrintTeam())
f.close()
