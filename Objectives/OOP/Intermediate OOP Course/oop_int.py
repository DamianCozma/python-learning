class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.number = numberOfStudents

  def get_name(self):
    return self.name
  def get_level(self):
    return self.level
  def get_numberOfStudents(self):
    return self.number

  def set_name(self, new_name):
    self.name = new_name
  def set_level(self, new_level):
    self.level = new_level
  def set_numberOfStudents(self, new_number):
    self.number = new_number

  def __repr__(self):
        return f'A {self.level} school named {self.name} with {self.number} students'

class PrimarySchool(School):
  def __init__(self, name, pickupPolicy, numberOfStudents):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    return super().__repr__() + f', the pickup policy is {self.pickupPolicy}.'

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams
  
  def get_sportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    return super().__repr__() + f'. Our sports team are: {self.sportsTeams}'
