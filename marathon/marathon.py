import bowler as b

bowlers = []

#import scores
f = open('scores.txt', 'r')
numBowlers = int(f.readline())
for i in range(numBowlers):
    name = f.readline()
    hdcp = int(f.readline())
    g1 = int(f.readline())
    g2 = int(f.readline())
    g3 = int(f.readline())
    g4 = int(f.readline())
    g5 = int(f.readline())
    g6 = int(f.readline())
    bowlers.append(b.Bowler(name, hdcp, g1, g2, g3, g4, g5, g6))
f.close()

#sort bowlers by total plus handicap
for i in range(numBowlers):
    for j in range(i, numBowlers):
        if bowlers[i] < bowlers[j]:
            temp = bowlers[i]
            bowlers[i] = bowlers[j]
            bowlers[j] = temp

#export standings
f = open('marathonStandings.txt', 'w')
for i in range(numBowlers):
    f.write(str(bowlers[i]) + '\n')
f.close()