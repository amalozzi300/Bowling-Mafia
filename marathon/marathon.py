import bowler as b

bowlerList = []

f = open("scores.txt", "r")

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
  g7 = int(f.readline())
  g8 = int(f.readline())

  bowlerList.append(b.Bowler(name, hdcp, g1, g2, g3, g4, g5, g6, g7, g8))

for i in range(numBowlers):
  for j in range(i, numBowlers):
    if bowlerList[i] < bowlerList[j]:
      temp = bowlerList[i]
      bowlerList[i] = bowlerList[j]
      bowlerList[j] = temp

for i in range(numBowlers):
  print(str(i + 1) + '. ' + str(bowlerList[i]))