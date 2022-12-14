import bowler as b
import team as t

teams = []

f = open('mdTeams.txt', 'r')
numTeams = int(f.readline())
for i in range(numTeams):
  name = f.readline()
  hdcp = int(f.readline())
  g1 = int(f.readline())
  g2 = int(f.readline())
  g3 = int(f.readline())
  g4 = int(f.readline())
  g5 = int(f.readline())
  g6 = int(f.readline())
  b1 = b.Bowler(name, hdcp, g1, g2, g3, g4, g5, g6)

  name = f.readline()
  hdcp = int(f.readline())
  g1 = int(f.readline())
  g2 = int(f.readline())
  g3 = int(f.readline())
  g4 = int(f.readline())
  g5 = int(f.readline())
  g6 = int(f.readline())
  b2 = b.Bowler(name, hdcp, g1, g2, g3, g4, g5, g6)

  teams.append(t.Team(b1, b2))
  temp = f.readline()
f.close()

for i in range(len(teams)):
  for j in range(len(teams)):
    if teams[j] < teams[i]:
      temp = teams[i]
      teams[i] = teams[j]
      teams[j] = temp

f = open('mdStandings.txt', 'w')
for i in range(numTeams):
  f.write(str(teams[i]) + '\n')
f.close()
