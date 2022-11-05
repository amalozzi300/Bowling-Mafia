import bowler as b

bowlers = []

numBowlers = int(input())

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

for i in range(numBowlers):
  bowlers[i].g1Format()

print()  
print('GAME 2:')

for i in range(numBowlers):
  for j in range(numBowlers):
    if bowlers[j].g2Less(bowlers[i]):
      temp = bowlers[i]
      bowlers[i] = bowlers[j]
      bowlers[j] = temp

for i in range(numBowlers):
  bowlers[i].g2Format()

print()
print('GAME 3:')

for i in range(numBowlers):
  for j in range(numBowlers):
    if bowlers[j].g3Less(bowlers[i]):
      temp = bowlers[i]
      bowlers[i] = bowlers[j]
      bowlers[j] = temp

for i in range(numBowlers):
  bowlers[i].g3Format()
