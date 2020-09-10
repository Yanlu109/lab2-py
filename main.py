# Author: Yanling Yan Lu yfl5541@psu.edu
# Collaborator: Gabrielle Brunner-King gsb5225@psu.edu
# Collaborator: Mason McGuirk (mtm5868@psu.edu)
# Section: 4
# Breakout: 13

def getLetterGrade(grade):
  if grade >= 93.0:
    lettergrade = 'A'
  elif grade >= 90.0:
    lettergrade = 'A-'
  elif grade >= 87.0:
    lettergrade = 'B+'
  elif grade >= 83.0:
    lettergrade = 'B'
  elif grade >= 80.0:
    lettergrade = 'B-'
  elif grade >= 77.0:
    lettergrade = 'C+'
  elif grade >= 70.0:
    lettergrade = 'C'
  elif grade >= 60:
    lettergrade = 'D'
  else:
    lettergrade = 'F'
  return lettergrade

def run():
  lettergrade = float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(lettergrade)}.")

if __name__=="__main__":
  run()
 