import bowler as b

bowlers = []
elim = []
hg = []
md = []

numBowlers = int(input())

for i in range(numBowlers):
  name = input()
  hdcp = int(input())
  inElim = int(input())
  inHG = int(input())
  inMD = int(input())

  b1 = b.Bowler(name, hdcp)

  bowlers.append(b1)

  if inElim == 1:
    elim.append(b1)

  if inHG == 1:
    hg.append(b1)

  if inMD > 0:
    for i in range(inMD):
      md.append(b1)

f = open("scores.txt", "w")
f.write(str(len(bowlers)) + '\n')
for i in range(len((bowlers))):
  f.write(bowlers[i].PrintBowler() + '\n')
f.close()

f = open("elimBowlers.txt", "w")
f.write(str(len(elim)) + '\n')
for i in range(len(elim)):
  f.write(elim[i].PrintBowler() + '\n')
f.close()

f = open("hgBowlers.txt", "w")
f.write(str(len(hg)) + '\n')
for i in range(len(hg)):
  f.write(hg[i].PrintBowler() + '\n')
f.close()

f = open("mdBowlers.txt", "w")
f.write(str(len(md)) + '\n')
for i in range(len(md)):
  f.write(md[i].PrintBowler() + '\n')
f.close()