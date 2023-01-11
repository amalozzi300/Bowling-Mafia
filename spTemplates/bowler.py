class Bowler:
  def __init__(self, name, hdcp = 0, g1 = 0, g2 = 0, g3 = 0):
    self.name = name.rstrip(name[-1])
    self.hdcp = hdcp
    self.g1 = g1
    self.g2 = g2
    self.g3 = g3

  def __eq__(self, bowler1):
    if self.name == bowler1.name:
      return True

    return False

  def __ne__(self, bowler1):
    return not(self == bowler1)

  def __str__(self):
    return f'{self.name}'

  def PrintBowler(self):
    return f'{self.name}\n{self.hdcp}\n{self.g1}\n{self.g2}\n{self.g3}'

  def Total(self):
    if self.g2 == 0:
      return self.hdcp + self.g1
    elif self.g3 == 0:
      return (2 * self.hdcp) + self.g1 + self.g2
    else:
      return (3 * self.hdcp) + self.g1 + self.g2 + self.g3

  def g1Less(self, bowler1):
    return (self.g1 + self.hdcp) < (bowler1.g1 + bowler1.hdcp)

  def g2Less(self, bowler1):
    return (self.g2 + self.hdcp) < (bowler1.g2 + bowler1.hdcp)

  def g3Less(self, bowler1):
    return (self.g3 + self.hdcp) < (bowler1.g3 + bowler1.hdcp)

  def g1Format(self):
    print(f'<li>{self.name}: {(self.g1 + self.hdcp)}</li>')
  
  def g2Format(self):
    print(f'<li>{self.name}: {(self.g2 + self.hdcp)}</li>')

  def g3Format(self):
    print(f'<li>{self.name}: {(self.g3 + self.hdcp)}</li>')