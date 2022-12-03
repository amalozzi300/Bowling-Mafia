import math
import bowler as b

bowlers = []
firstAdvancers = []
secondAdvancers = []

numBowlers = int(input())

if numBowlers % 2 == 1:
  g1Cut = math.floor(numBowlers / 2) + 1
else:
  g1Cut = numBowlers / 2

if g1Cut % 2 == 1:
  g2Cut = math.floor(g1Cut / 2) + 1
else:
  g2Cut = g1Cut / 2

if numBowlers < 11:
  numPaid = 2
elif numBowlers < 18:
  numPaid = 3
elif numBowlers < 31:
  numPaid = 4
else:
  numPaid = 5

cutScore = 0

for i in range(numBowlers):
  name = input()
  hdcp = int(input())
  g1 = int(input())
  g2 = int(input())
  g3 = int(input())

  bowlers.append(b.Bowler(name, hdcp, g1, g2, g3))

print('GAME 1:')

for i in range(numBowlers):
  for j in range(numBowlers):
    if bowlers[j].g1Less(bowlers[i]):
      temp = bowlers[i]
      bowlers[i] = bowlers[j]
      bowlers[j] = temp

cutScore = (bowlers[int(g1Cut - 1)].g1 + bowlers[int(g1Cut - 1)].hdcp)

for i in range(int(g1Cut), numBowlers):
  if (bowlers[i].g1 + bowlers[i].hdcp) == cutScore:
    g1Cut += 1
  else:
    break

for i in range(numBowlers):
  bowlers[i].g1Format()

  if i < g1Cut:
    firstAdvancers.append(bowlers[i])

  if i == (g1Cut - 1):
    print('--------------------------------------')

print()  
print('GAME 2:')

for i in range(len(firstAdvancers)):
  for j in range(len(firstAdvancers)):
    if firstAdvancers[j].g2Less(firstAdvancers[i]):
      temp = firstAdvancers[i]
      firstAdvancers[i] = firstAdvancers[j]
      firstAdvancers[j] = temp

cutScore = (firstAdvancers[int(g2Cut - 1)].g2 + firstAdvancers[int(g2Cut - 1)].hdcp)

for i in range(int(g2Cut), len(firstAdvancers)):
  if (firstAdvancers[i].g2 + firstAdvancers[i].hdcp) == cutScore:
    g2Cut += 1
  else:
    break

for i in range(len(firstAdvancers)):
  firstAdvancers[i].g2Format()

  if i < g2Cut:
    secondAdvancers.append(firstAdvancers[i])

  if i == (g2Cut - 1):
    print('--------------------------------------')

print()
print('GAME 3:')

for i in range(len(secondAdvancers)):
  for j in range(len(secondAdvancers)):
    if secondAdvancers[j].g3Less(secondAdvancers[i]):
      temp = secondAdvancers[i]
      secondAdvancers[i] = secondAdvancers[j]
      secondAdvancers[j] = temp

for i in range(len(secondAdvancers)):
  secondAdvancers[i].g3Format()

  if i == (numPaid - 1):
    print('--------------------------------------')