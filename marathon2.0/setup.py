import bowler as b

bowlers = []
#include rest of sidepot lists here

#import bowlers
f = open('bowlers.txt', 'r')
numBowlers = int(f.readline())
for i in range(numBowlers):
    name = f.readline()
    hdcp = int(f.readline())

    b1 = b.Bowler(name, hdcp)

    bowlers.append(b1)
f.close()

#export bowlers to score.txt
f = open('scores.txt', 'w')
f.write(str(len(bowlers)) + '\n')
for i in range(len(bowlers)):
    f.write(bowlers[i].printBowler() + '\n')
f.close()

#export to other sidepots here