import bowler as b
import team as t

teamList = []

f = open("1.txt", "r")

numTeams = int(f.readline())

for num in range(numTeams):
  temp = f.readline()
  teamName = f.readline()
  b1 = f.readline()
  b1Hdcp = int(f.readline())
  b2 = f.readline()
  b2Hdcp = int(f.readline())
  b3 = f.readline()
  b3Hdcp = int(f.readline())

  teamList.append(t.Team(teamName, b.Bowler(b1, b1Hdcp), b.Bowler(b2, b2Hdcp), b.Bowler(b3, b3Hdcp)))

f.close()

f = open("2.txt", "r")

numSquad = int(f.readline())
numTeams += numSquad

for num in range(numSquad):
  temp = f.readline()
  teamName = f.readline()
  b1 = f.readline()
  b1Hdcp = int(f.readline())
  b2 = f.readline()
  b2Hdcp = int(f.readline())
  b3 = f.readline()
  b3Hdcp = int(f.readline())

  teamList.append(t.Team(teamName, b.Bowler(b1, b1Hdcp), b.Bowler(b2, b2Hdcp), b.Bowler(b3, b3Hdcp)))

f.close()

f = open("3.txt", "r")

numSquad = int(f.readline())
numTeams += numSquad

for num in range(numSquad):
  temp = f.readline()
  teamName = f.readline()
  b1 = f.readline()
  b1Hdcp = int(f.readline())
  b2 = f.readline()
  b2Hdcp = int(f.readline())
  b3 = f.readline()
  b3Hdcp = int(f.readline())

  teamList.append(t.Team(teamName, b.Bowler(b1, b1Hdcp), b.Bowler(b2, b2Hdcp), b.Bowler(b3, b3Hdcp)))

f.close()

f = open("4.txt", "r")

numSquad = int(f.readline())
numTeams += numSquad

for num in range(numSquad):
  temp = f.readline()
  teamName = f.readline()
  b1 = f.readline()
  b1Hdcp = int(f.readline())
  b2 = f.readline()
  b2Hdcp = int(f.readline())
  b3 = f.readline()
  b3Hdcp = int(f.readline())

  teamList.append(t.Team(teamName, b.Bowler(b1, b1Hdcp), b.Bowler(b2, b2Hdcp), b.Bowler(b3, b3Hdcp)))

f.close()

f = open("5.txt", "r")

numSquad = int(f.readline())
numTeams += numSquad

for num in range(numSquad):
  temp = f.readline()
  teamName = f.readline()
  b1 = f.readline()
  b1Hdcp = int(f.readline())
  b2 = f.readline()
  b2Hdcp = int(f.readline())
  b3 = f.readline()
  b3Hdcp = int(f.readline())

  teamList.append(t.Team(teamName, b.Bowler(b1, b1Hdcp), b.Bowler(b2, b2Hdcp), b.Bowler(b3, b3Hdcp)))

f.close()

f = open("6.txt", "r")

numSquad = int(f.readline())
numTeams += numSquad

for num in range(numSquad):
  temp = f.readline()
  teamName = f.readline()
  b1 = f.readline()
  b1Hdcp = int(f.readline())
  b2 = f.readline()
  b2Hdcp = int(f.readline())
  b3 = f.readline()
  b3Hdcp = int(f.readline())

  teamList.append(t.Team(teamName, b.Bowler(b1, b1Hdcp), b.Bowler(b2, b2Hdcp), b.Bowler(b3, b3Hdcp)))

f.close()

print(numTeams)
print()

for num in range(numTeams):
  teamList[num].PrintTeam()