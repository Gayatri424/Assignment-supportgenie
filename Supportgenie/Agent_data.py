class Agent:
 def __init__(self,is_available,available_since,roles):
  self.is_available=is_available
  time=available_since
  h, m = map(int, time.split(':'))
  self.available_since=h*60+m
  self.roles=roles
 
