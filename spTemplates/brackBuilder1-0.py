import bowler as b
import math

bowlers = []
shortBowlers = []
countList = []

f = open('bracketBowlers.txt', 'r')
numBowlers = int(f.readline())
for i in range(numBowlers):
  name = f.readline()
  hdcp = int(f.readline())
  b1 = b.Bowler(name, hdcp)
  bowlers.append(b1)
f.close()

minBracks = math.ceil(numBowlers / 8)

print('Total Bracket Bowlers: ' + str(numBowlers))
print('Minimum Number of Brackets: ' + str(minBracks) + '\n')

curr = bowlers[0]
count = 1
for i in range(1, numBowlers):
  if curr == bowlers[i]:
    count += 1
  else:
    print(curr.name + ':\t' + str(count))
    shortBowlers.append(curr)
    countList.append(count)
    curr = bowlers[i]
    count = 1
print(curr.name + ':\t' + str(count))
shortBowlers.append(curr)
countList.append(count)

#remove bowlers in too many brackets
