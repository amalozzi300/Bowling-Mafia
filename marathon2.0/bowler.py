class Bowler:
  def __init__(self, name, hdcp = 0, g1 = 0, g2 = 0, g3 = 0, g4 = 0, g5 = 0, g6 = 0):
    self.name = name
    self.hdcp = hdcp
    self.g1 = g1
    self.g2 = g2
    self.g3 = g3
    self.g4 = g4
    self.g5 = g5
    self.g6 = g6

  def __eq__(self, bowler1):
    if self.name == bowler1.name:
      return True

    return False

  def __ne__(self, bowler1):
    return not(self == bowler1)

  def __lt__(self, bowler1):
    return self.Total() < bowler1.Total()

  def __str__(self):
    return f'{self.name}\t\t{self.hdcp}\t\t{self.g1}\t{self.g2}\t{self.g3}\t{self.g4}\t{self.g5}\t{self.g6}\t--\t{self.Total()}'

  def PrintBowler(self):
    return f'{self.name}{self.hdcp}\n{self.g1}\n{self.g2}\n{self.g3}\n{self.g4}\n{self.g5}\n{self.g6}'

  def Total(self):
    if self.g1 == 0:
      return self.hdcp
    elif self.g2 == 0:
      return self.hdcp + self.g1
    elif self.g3 == 0:
      return (2 * self.hdcp) + self.g1 + self.g2
    elif self.g4 == 0:
      return (3 * self.hdcp) + self.g1 + self.g2 + self.g3
    elif self.g5 == 0:
      return (4 * self.hdcp) + self.g1 + self.g2 + self.g3 + self.g4
    elif self.g6 == 0:
      return (5 * self.hdcp) + self.g1 + self.g2 + self.g3 + self.g4 + self.g5
    else:
      return (6 * self.hdcp) + self.g1 + self.g2 + self.g3 + self.g4 + self.g5 + self.g6

  def g1Less(self, bowler1):
    return (self.g1 + self.hdcp) < (bowler1.g1 + bowler1.hdcp)

  def g2Less(self, bowler1):
    return (self.g2 + self.hdcp) < (bowler1.g2 + bowler1.hdcp)

  def g3Less(self, bowler1):
    return (self.g3 + self.hdcp) < (bowler1.g3 + bowler1.hdcp)

  def g4Less(self, bowler1):
    return (self.g4 + self.hdcp) < (bowler1.g4 + bowler1.hdcp)

  def g5Less(self, bowler1):
    return(self.g5 + self.hdcp) < (bowler1.g5 + bowler1.hdcp)

  def g6Less(self, bowler1):
    return(self.g6 + self.hdcp) < (bowler1.g6 + bowler1.hdcp)

  def g1Equal(self, bowler1):
    return (self.g1 + self.hdcp) == (bowler1.g1 + bowler1.hdcp)

  def g2Equal(self, bowler1):
    return (self.g2 + self.hdcp) == (bowler1.g2 + bowler1.hdcp)

  def g3Equal(self, bowler1):
    return (self.g3 + self.hdcp) == (bowler1.g3 + bowler1.hdcp)

  def g4Equal(self, bowler1):
    return (self.g4 + self.hdcp) == (bowler1.g4 + bowler1.hdcp)

  def g5Equal(self, bowler1):
    return(self.g5 + self.hdcp) == (bowler1.g5 + bowler1.hdcp)

  def g6Equal(self, bowler1):
    return(self.g6 + self.hdcp) == (bowler1.g6 + bowler1.hdcp)

  def g1Format(self):
    print(f'<li>{self.name}: {(self.g1 + self.hdcp)}</li>')
  
  def g2Format(self):
    print(f'<li>{self.name}: {(self.g2 + self.hdcp)}</li>')

  def g3Format(self):
    print(f'<li>{self.name}: {(self.g3 + self.hdcp)}</li>')

  def g4Format(self):
    print(f'<li>{self.name}: {(self.g4 + self.hdcp)}</li>')

  def g5Format(self):
    print(f'<li>{self.name}: {(self.g5 + self.hdcp)}</li>')

  def g6Format(self):
    print(f'<li>{self.name}: {(self.g6 + self.hdcp)}</li>')