import bowler as b

bowlerList = []
elim1List = []
elim2List = []
hgList = []
wtaList = []
md1List = []
md2List = []

f = open("bowlers.txt", "r")

numBowlers = int(f.readline())

for i in range(numBowlers):
  name = f.readline()
  hdcp = int(f.readline())
  sidepots = int(f.readline())

  b1 = b.Bowler(name, hdcp)
  bowlerList.append(b1)

  if sidepots == 0:
    continue

  elim1 = int(f.readline())
  elim2 = int(f.readline())
  hg = int(f.readline())
  wta = int(f.readline())
  md1 = int(f.readline())
  md2 = int(f.readline())

  if elim1:
    elim1List.append(b1)
  if elim2:
    elim2List.append(b1)
  if hg:
    hgList.append(b1)
  if wta:
    wtaList.append(b1)
  if md1 > 0:
    for i in range(md1):
      md1List.append(b1)
  if md2 > 0:
    for i in range(md2):
      md2List.append(b1)

f.close()

f = open("scores.txt", "w")
f.write(str(numBowlers) + '\n')
for i in range(numBowlers):
  f.write(bowlerList[i].PrintBowler() + '\n')
f.close()

f = open("elim1Bowlers.txt", "w")
f.write(str(len(elim1List)) + '\n')
for i in range(len(elim1List)):
  f.write(elim1List[i].PrintBowler() + '\n')
f.close()

f = open("elim2Bowlers.txt", "w")
f.write(str(len(elim2List)) + '\n')
for i in range(len(elim2List)):
  f.write(elim2List[i].PrintBowler() + '\n')
f.close()

f = open("hgBowlers.txt", "w")
f.write(str(len(hgList)) + '\n')
for i in range(len(hgList)):
  f.write(hgList[i].PrintBowler() + '\n')
f.close()

f = open("wtaBowlers.txt", "w")
f.write(str(len(wtaList)) + '\n')
for i in range(len(wtaList)):
  f.write(wtaList[i].PrintBowler() + '\n')
f.close()

f = open("md1Bowlers.txt", "w")
f.write(str(len(md1List)) + '\n')
for i in range(len(md1List)):
  f.write(md1List[i].PrintBowler() + '\n')
f.close()

f = open("md2Bowlers.txt", "w")
f.write(str(len(md2List)) + '\n')
for i in range(len(md2List)):
  f.write(md2List[i].PrintBowler() + '\n')
f.close()