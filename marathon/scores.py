import bowler as b

bowlers = []
mdNames = []

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

#export scores to mystery doubles files here
f = open("mdTeams.txt", "r")
numBowlers = int(f.readline())
for i in range(numBowlers * 2):
  name = f.readline()
  temp = int(f.readline())
  temp = int(f.readline())
  temp = int(f.readline())
  temp = int(f.readline())
  temp = int(f.readline())
  temp = int(f.readline())
  temp = int(f.readline())
  mdNames.append(b.Bowler(name, temp))
  if i % 2 == 1:
    f.readline()
f.close()

f = open("mdTeams.txt", "w")
f.write(str(numBowlers) + "\n")
for i in range(numBowlers * 2):
  for j in range(len(bowlers)):
    if mdNames[i].name == bowlers[j].name:
      f.write(bowlers[j].printBowler() + "\n")
  if i % 2 == 1:
    f.write("\n")
f.close()