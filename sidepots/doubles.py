import bowler as b
import team as t

teams = []

numTeams = int(input())

for i in range(numTeams):
  name = input()
  hdcp = int(input())
  g1 = int(input())
  g2 = int(input())
  g3 = int(input())

  b1 = b.Bowler(name, hdcp, g1, g2, g3)

  name = input()
  hdcp = int(input())
  g1 = int(input())
  g2 = int(input())
  g3 = int(input())

  b2 = b.Bowler(name, hdcp, g1, g2, g3)

  teams.append(t.Team(b1, b2))

  temp = input()

for i in range(len(teams)):
  for j in range(len(teams)):
    if teams[j] < teams[i]:
      temp = teams[i]
      teams[i] = teams[j]
      teams[j] = temp


for i in range(numTeams):
  print(teams[i])

