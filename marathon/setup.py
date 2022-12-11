import bowler as b

bowlers = []
doubles = []

#import bowlers
f = open('bowlers.txt', 'r')
numBowlers = int(f.readline())
for i in range(numBowlers):
    name = f.readline()
    hdcp = int(f.readline())
    numEntries = int(f.readline())
    b1 = b.Bowler(name, hdcp)
    bowlers.append(b1)
    if numEntries > 0:
        for i in range(numEntries):
            doubles.append(b1)
f.close()

#export bowlers to score.txt
f = open('scores.txt', 'w')
f.write(str(len(bowlers)) + '\n')
for i in range(len(bowlers)):
    f.write(bowlers[i].printBowler() + '\n')
f.close()

#export to mystery doubles here
f = open('mdBowlers.txt', 'w')
f.write(str(len(doubles)) + '\n')
for i in range(len(doubles)):
    f.write(doubles[i].name + '\n')
    f.write(str(doubles[i].hdcp) + '\n')
f.close()