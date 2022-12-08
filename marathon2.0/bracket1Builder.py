import bowler as b
import random
import math

bowlers = []
brackets = []

f = open('bracket1Bowlers.txt', 'r')
numBowlers = int(f.readline())
for i in range(numBowlers):
  name = f.readline()
  hdcp = int(f.readline())
  b1 = b.Bowler(name, hdcp)
  bowlers.append(b1)
f.close()

numBracks = int(numBowlers / 8)
if numBowlers & 8 != 0:
  numBracks += 1



f = open('bracket1.txt', 'w')
f.write(str(numBracks))
for i in range(len(brackets)):
  for j in range(len(brackets[i])):
    f.write(str(brackets[i][j]) + '\n')
  f.write('\n\n')
f.close()