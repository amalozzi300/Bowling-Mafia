from unicodedata import name
import bowler as b
import team as t

teamList = []
bowlers = []

f = open("scores.txt", "r")

numTeams = int(f.readline())

for num in range(numTeams):
  temp = f.readline()
  teamName = f.readline()

  for i in range(3):
    name = f.readline()
    hdcp = int(f.readline())
    g1 = int(f.readline())
    g2 = int(f.readline())
    g3 = int(f.readline())
    g4 = int(f.readline())
    g5 = int(f.readline())

    bowlers.append(b.Bowler(name, hdcp, g1, g2, g3, g4, g5))

  teamList.append(t.Team(teamName, bowlers[0], bowlers[1], bowlers[2]))

  bowlers.clear()

for i in range(numTeams):
  for j in range(i, numTeams):
    if teamList[i] < teamList[j]:
      temp = teamList[i]
      teamList[i] = teamList[j]
      teamList[j] = temp

for num in range(numTeams):
  print(num + 1)
  print(teamList[num])