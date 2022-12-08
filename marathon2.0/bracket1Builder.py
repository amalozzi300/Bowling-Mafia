import bowler as b

pairs = []
brackets = []

f = open('bracket1Pairs.txt', 'r')
numPairs = int(f.readline())
for i in range(numPairs):
  temp = f.readline()
  name1 = f.readline()
  hdcp1 = int(f.readline())
  name2 = f.readline()
  hdcp2 = int(f.readline())
  b1 = b.Bowler(name1, hdcp1)
  b2 = b.Bowler(name2, hdcp2)
  p = [b1, b2]
  pairs.append(p)
f.close()

print(pairs[0][0])
print(pairs[0][1])

brackets.append([pairs[0][0], pairs[0][1]])

for i in range(1, len(pairs)):
  p = pairs[i]
  added = False
  
  for j in range(len(brackets)):
    b = brackets[j]
    inB = False

    if not added and len(b) != 8:
      for k in range(len(b)):
        if p[0] == b[k] or p[1] == b[k]:
          inB = True
  
    if not inB:
      b.append(p[0])
      b.append(p[1])
      added = True

  if not added:
    brackets.append([p[0], p[1]])


f = open('bracket1.txt', 'w')
for i in range(len(brackets)):
  for j in range(len(brackets[i])):
    f.write(str(brackets[i][j]) + '\n')
  f.write('\n\n')
f.close()