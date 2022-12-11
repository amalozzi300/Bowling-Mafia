import bowler as b
import random
import math

def MyRandom(numBracks):
    return math.floor(random.random() * numBracks)

bowlers = []
brackets = []
pairs = []
unusedPairs = []

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

for i in range(numBracks):
  brackets.append([])

for b1 in bowlers:
  inB = True

  while inB:
    randNum = MyRandom(numBracks)
    inB = False

    for i in range(len(brackets[randNum])):
      if b1 == brackets[randNum][i]:
        inB = True

    if not inB:
      brackets[randNum].append(b1)

for br in brackets:
  for i in range(len(br)):
    if i % 2 == 0:
      p = [br[i], br[i + 1]]

      if len(pairs) == 0:
        pairs.append(p)
      else:
        for j in range(len(pairs)):
          if (p[0] == pairs[j][0] or p[0] == pairs[j][1]) and (p[1] == pairs[j][0] or p[1] == pairs[j][1]):
            br.remove(p[0])
            br.remove(p[1])
            unusedPairs.append(p)

f = open('bracket1.txt', 'w')
f.write(str(numBracks) + '\n')
for i in range(len(brackets)):
  for j in range(len(brackets[i])):
    f.write(str(brackets[i][j]) + '\n')
  f.write('\n\n')
f.write('\n\n')
for i in range(len(unusedPairs)):
  f.write(str(pairs[i][0]) + '\n')
  f.write(str(pairs[i][1]) + '\n')
  f.write('\n')
f.close()