class Team:
  def __init__(self, teamName, bowler1, bowler2, bowler3):
    self.teamName = teamName
    self.bowler1 = bowler1
    self.bowler2 = bowler2
    self.bowler3 = bowler3
    self.hdcp = bowler1.hdcp + bowler2.hdcp + bowler3.hdcp

  def __lt__(self, team1):
    return self.Total() < team1.Total()

  def __str__(self):
    teamString = self.teamName
    teamString += f'\t{self.bowler1.name}\t\t{self.bowler1.hdcp}\t{self.bowler1.g1}\t{self.bowler1.g2}\t{self.bowler1.g3}\t{self.bowler1.g4}\t{self.bowler1.g5}\n'
    teamString += f'\t{self.bowler2.name}\t\t{self.bowler2.hdcp}\t{self.bowler2.g1}\t{self.bowler2.g2}\t{self.bowler2.g3}\t{self.bowler2.g4}\t{self.bowler2.g5}\n'
    teamString += f'\t{self.bowler3.name}\t\t{self.bowler3.hdcp}\t{self.bowler3.g1}\t{self.bowler3.g2}\t{self.bowler3.g3}\t{self.bowler3.g4}\t{self.bowler3.g5}\n'
    return teamString

  def PrintTeam(self):
    print(f'{self.teamName}{self.bowler1.PrintBowler()}\n{self.bowler2.PrintBowler()}\n{self.bowler3.PrintBowler()}\n')

  def Total(self):
    return self.bowler1.Total() + self.bowler2.Total() + self.bowler3.Total()