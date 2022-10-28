class Team:
  def __init__(self, bowler1, bowler2):
    self.bowler1 = bowler1
    self.bowler2 = bowler2

  def __eq__(self, team1):
    if self.bowler1 == team1.bowler1 or self.bowler1 == team1.bowler2:
      if self.bowler2 == team1.bowler1 or self.bowler2 == team1.bowler2:
        return True
    
    return False

  def __ne__(self, team1):
    return not(self == team1)

  def __lt__(self, team1):
    return self.Total() < team1.Total()

  def __str__(self):
    return f'<li>{self.bowler1} + {self.bowler2}: {self.Total()}</li>'

  def PrintTeam(self):
    print(f'{self.bowler1.PrintBowler()}\n{self.bowler2.PrintBowler()}\n')

  def Total(self):
    return self.bowler1.Total() + self.bowler2.Total()