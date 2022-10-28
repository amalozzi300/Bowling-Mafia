import bowler as b

bowlers = []
elimNames = []
hgNames = []
mdNames = []

f = open("scores.txt", "r")

numBowlers = int(input())
numBowlers1 = int(f.readline())

for i in range(numBowlers):
  name = input()
  name1 = f.readline()
  hdcp = int(input())
  hdcp1 = int(f.readline())
  elim =int(input())
  hg = int(input())
  md = int(input())
  g1 = int(f.readline())
  g2 = int(f.readline())
  g3 = int(f.readline())

  b1 = b.Bowler(name, hdcp, g1, g2, g3)

  bowlers.append(b1)
f.close()

f = open("elimBowlers.txt", "r")
numBowlers = int(f.readline())
for i in range(numBowlers):
  name = f.readline()
  name = name.rstrip(name[-1])
  temp = int(f.readline())
  temp = int(f.readline())
  temp = int(f.readline())
  temp = int(f.readline())

  elimNames.append(name)
f.close()

f = open("elimBowlers.txt", "w")
f.write(str(numBowlers) + "\n")
for i in range(numBowlers):
  for j in range(len(bowlers)):
    if elimNames[i] == bowlers[j].name:
      f.write(bowlers[j].PrintBowler() + "\n")
f.close()

f = open("hgBowlers.txt", "r")
numBowlers = int(f.readline())
for i in range(numBowlers):
  name = f.readline()
  name = name.rstrip(name[-1])
  temp = int(f.readline())
  temp = int(f.readline())
  temp = int(f.readline())
  temp = int(f.readline())

  hgNames.append(name)
f.close()

f = open("hgBowlers.txt", "w")
f.write(str(numBowlers) + "\n")
for i in range(numBowlers):
  for j in range(len(bowlers)):
    if hgNames[i] == bowlers[j].name:
      f.write(bowlers[j].PrintBowler() + "\n")
f.close()

f = open("mdTeams.txt", "r")
numBowlers = int(f.readline())
for i in range(numBowlers * 2):
  name = f.readline()
  name = name.rstrip(name[-1])
  temp = int(f.readline())
  temp = int(f.readline())
  temp = int(f.readline())
  temp = int(f.readline())

  mdNames.append(name)

  if i % 2 == 1:
    f.readline()
f.close()

f = open("mdTeams.txt", "w")
f.write(str(numBowlers) + "\n")
for i in range(numBowlers * 2):
  for j in range(len(bowlers)):
    if mdNames[i] == bowlers[j].name:
      f.write(bowlers[j].PrintBowler() + "\n")

  if i % 2 == 1:
    f.write("\n")
f.close()
