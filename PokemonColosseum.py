import random
import csv

def get_pokemon_data(pokemon_id):
    with open('pokemon-data.csv', 'r') as f:
        i = 0
        reader = csv.reader(f)
        for row in reader:
          if i == pokemon_id:
              return row
          i = i + 1
    return None

def TypeE(moveT, oppT):
  if(moveT == "Normal" or oppT == "Normal"):
    return 1
  if(moveT == "Fire"):
    if(oppT == "Fire"):
      return .5
    if(oppT == "Water"):
      return .5
    if(oppT == "Grass"):
      return .5
    return 1
  if(moveT == "Water"):
    if(oppT == "Fire"):
      return 2
    if(oppT == "Water"):
      return .5
    if(oppT == "Grass"):
      return .5
    return 1
  if(moveT == "Electric"):
    if(oppT == "Electric"):
      return .5
    if(oppT == "Water"):
      return 2
    if(oppT == "Grass"):
      return .5
    return 1
  if(moveT == "Grass"):
    if(oppT == "Fire"):
      return .5
    if(oppT == "Water"):
      return 2
    if(oppT == "Grass"):
      return .5
    return 1


  return 1

class Pokemon():
  def init(self, name, pType, pHP, pAttack, pDefence, pHeight, pWeight, pMoves): 
    self.name = name
    self.Type = pType
    self.HP = int(pHP)
    self.Attack = int(pAttack)
    self.Defense = int(pDefence)
    self.height = int(pHeight)
    self.weight = int(pWeight)
    self.Moves = pMoves

def Damage(move, pokemon1, pokemon2):
  moveList = MoveSearch(move)
  power = moveList[5]
  STAB = 1.0
  if moveList[1] == pokemon1.Type:
    STAB = 1.5

  k = random.randint(5,10)
  k = k /10

  j = TypeE(moveList[1], pokemon2.Type)
  
  total = int(power) * (pokemon1.Attack / pokemon2.Defense) * STAB * j * k
  total = int(total) + 1
  return total

def MoveSearch(move):
  with open('moves-data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
          if move == row[0]:
              return row
  return None

def parse(pokemon, string):
  x = string
  Pokemon.init(pokemon, x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7])

def teamMake(a, b, c):
  P1 = Pokemon() #Rocket pokemon generation
  P2 = Pokemon()
  P3 = Pokemon()
  string = get_pokemon_data(a)
  parse(P1, string)
  string = get_pokemon_data(b)
  parse(P2, string)
  string = get_pokemon_data(c)
  parse(P3, string)
  List = []
  List.append(P1)
  List.append(P2)
  List.append(P3)
  return List
  
##############################Main#######################
print("Welcome to Pokemon Stadium")
name = input("\nEnter Player Name: ")

a = [0] * 6
index = 0
for x in a:
  i = random.randint(1,82)
  k = 0
  while(k == 0):
    if i not in a:
      k = 1
    else:
      k = 0
      i = random.randint(1,82)
  
  a[index] = i
  index = index + 1

rocketList = teamMake(a[0], a[1], a[2])
userList = teamMake(a[3], a[4], a[5])


print("\nTeam Rocket enters with", '{0}, {1}, {2}.'.format(rocketList[0].name, rocketList[1].name, rocketList[2].name))
print("\nTeam", name, "enters with", '{0}, {1}, {2}.'.format(userList[0].name, userList[1].name, userList[2].name))

j = random.randint(1,2)


useMove = [0, 0, 0, 0, 0]
rockMove = [0, 0, 0, 0, 0]
uI = 0
rI = 0

if(j == 1):
  print("\nLet the battle begin!\nThe coin toss goes to Team Rocket\n")
else:
  print("\nLet the battle begin!\nThe coin toss goes to Team", name, "\n")

  
  print("\n---------------------------------------------")
  print("| Team Rocket   Name           HP           |")
  print("|              ",'{:<12}'.format(rocketList[rI].name), '{:>4}'.format(rocketList[rI].HP), "          |")
  print("|                                           |")
  print("| Team", '{:<8}'.format(name), "Name           HP           |")
  print("|              ",'{:<12}'.format(userList[uI].name), '{:>4}'.format(userList[uI].HP), "          |")
  print("---------------------------------------------")
  
  x = userList[uI].Moves
  x = x.replace('[', '')
  x = x.replace(']', '')
  x = x.replace("'", '')
  y = x.split(",")

  index = 0
  for x in y:
    if(x[0] == ' '):
      y[index] = y[index].replace(' ', '', 1)
    if(useMove[index] == 0):
      print('{0}. {1}'.format(index+1, y[index]))
    else:
      print('{0}.'.format(index+1),'{:<16}'.format(y[index]), "(N/A)")
    index = 1 + index

  while(1 > 0):
    if(useMove == [1, 1, 1, 1, 1]):
      useMove = [0, 0, 0, 0, 0]
    MoveInput = int(input("\nTeam {0}'s choice: ".format(name)))
    
    if (MoveInput == 1):
      if(useMove[0] == 0):
        useMove[0] = 1
        damage = Damage(y[0], userList[uI], rocketList[rI])
        break;
    elif (MoveInput == 2):
      if(useMove[1] == 0):
        useMove[1] = 1
        damage = Damage(y[1], userList[uI], rocketList[rI])
        break;
    elif (MoveInput == 3):
      if(useMove[2] == 0):
        useMove[2] = 1
        damage = Damage(y[2], userList[uI], rocketList[rI])
        break;
    elif (MoveInput == 4):
      if(useMove[3] == 0):
        useMove[3] = 1
        damage =  Damage(y[3], userList[uI], rocketList[rI])
        break;
    elif (MoveInput == 5):
      if(useMove[4] == 0):
        useMove[4] = 1
        damage =  Damage(y[4], userList[uI], rocketList[rI])
        break;
    print("\nInvalid input")

  print("\n{0}".format(userList[uI].name), "used {0} on {1} and did {2} points of damage.".format(y[MoveInput - 1], rocketList[rI].name, damage))
  
  rocketList[rI].HP = rocketList[rI].HP - damage

  if(rocketList[rI].HP <= 0):
    print("\n{0} has fainted!".format(rocketList[rI].name))
    if(rI == 2):
      print("\nTeam Rocket has no more usable pokemon, Team {0} is the victor!".format(name))
      exit(0)
    else: 
      rockMove = [0, 0, 0, 0, 0]
      rI = rI + 1
      print("\nTeam Rocket sends out {0}!".format(rocketList[rI].name))
###############################################################################
while(1 > 0):
  print("\n---------------------------------------------")
  print("| Team Rocket   Name           HP           |")
  print("|              ",'{:<12}'.format(rocketList[rI].name), '{:>4}'.format(rocketList[rI].HP), "          |")
  print("|                                           |")
  print("| Team", '{:<8}'.format(name), "Name           HP           |")
  print("|              ",'{:<12}'.format(userList[uI].name), '{:>4}'.format(userList[uI].HP), "          |")
  print("---------------------------------------------")

  x = rocketList[rI].Moves
  x = x.replace('[', '')
  x = x.replace(']', '')
  x = x.replace("'", '')
  y = x.split(",")

  index = 0
  for x in y:
    if(x[0] == ' '):
      y[index] = y[index].replace(' ', '', 1)
    index = 1 + index

  while(1 > 0):
    if(rockMove == [1, 1, 1, 1, 1]):
      rockMove = [0, 0, 0, 0, 0]
    MoveInput = random.randint(1,5)
    
    if (MoveInput == 1):
      if(rockMove[0] == 0):
        rockMove[0] = 1
        damage = Damage(y[0], rocketList[rI], userList[uI])
        break;
    elif (MoveInput == 2):
      if(rockMove[1] == 0):
        rockMove[1] = 1
        damage = Damage(y[1], rocketList[rI], userList[uI])
        break;
    elif (MoveInput == 3):
      if(rockMove[2] == 0):
        rockMove[2] = 1
        damage = Damage(y[2], rocketList[rI], userList[uI])
        break;
    elif (MoveInput == 4):
      if(rockMove[3] == 0):
        rockMove[3] = 1
        damage =  Damage(y[3], rocketList[rI], userList[uI])
        break;
    elif (MoveInput == 5):
      if(rockMove[4] == 0):
        rockMove[4] = 1
        damage =  Damage(y[4], rocketList[rI], userList[uI])
        break;
        
  print("\n{0}".format(rocketList[rI].name), "used {0} on {1} and did {2} points of damage.".format(y[MoveInput - 1], userList[uI].name, damage))
  
  userList[uI].HP = userList[uI].HP - damage

  if(userList[uI].HP <= 0):
    print("\n{0} has fainted!".format(userList[uI].name))
    if(uI == 2):
      print("\nTeam {0} has no more usable pokemon, Team Rocket is the victor!".format(name))
      exit(0)
    else: 
      useMove = [0, 0, 0, 0, 0]
      uI = uI + 1
      print("\nTeam {0} sends out {1}!".format(name, userList[uI].name))
    #################################################################################################

  print("\n---------------------------------------------")
  print("| Team Rocket   Name           HP           |")
  print("|              ",'{:<12}'.format(rocketList[rI].name), '{:>4}'.format(rocketList[rI].HP), "          |")
  print("|                                           |")
  print("| Team", '{:<8}'.format(name), "Name           HP           |")
  print("|              ",'{:<12}'.format(userList[uI].name), '{:>4}'.format(userList[uI].HP), "          |")
  print("---------------------------------------------")
  
  x = userList[uI].Moves
  x = x.replace('[', '')
  x = x.replace(']', '')
  x = x.replace("'", '')
  y = x.split(",")

  index = 0
  for x in y:
    if(x[0] == ' '):
      y[index] = y[index].replace(' ', '', 1)
    if(useMove[index] == 0):
      print('{0}. {1}'.format(index+1, y[index]))
    else:
      print('{0}.'.format(index+1),'{:<16}'.format(y[index]), "(N/A)")
    index = 1 + index

  while(1 > 0):
    if(useMove == [1, 1, 1, 1, 1]):
      useMove = [0, 0, 0, 0, 0]
    MoveInput = int(input("\nTeam {0}'s choice: ".format(name)))
    
    if (MoveInput == 1):
      if(useMove[0] == 0):
        useMove[0] = 1
        damage = Damage(y[0], userList[uI], rocketList[rI])
        break;
    elif (MoveInput == 2):
      if(useMove[1] == 0):
        useMove[1] = 1
        damage = Damage(y[1], userList[uI], rocketList[rI])
        break;
    elif (MoveInput == 3):
      if(useMove[2] == 0):
        useMove[2] = 1
        damage = Damage(y[2], userList[uI], rocketList[rI])
        break;
    elif (MoveInput == 4):
      if(useMove[3] == 0):
        useMove[3] = 1
        damage =  Damage(y[3], userList[uI], rocketList[rI])
        break;
    elif (MoveInput == 5):
      if(useMove[4] == 0):
        useMove[4] = 1
        damage =  Damage(y[4], userList[uI], rocketList[rI])
        break;
    print("\nInvalid input")

  print("\n{0}".format(userList[uI].name), "used {0} on {1} and did {2} points of damage.".format(y[MoveInput - 1], rocketList[rI].name, damage))
  
  rocketList[rI].HP = rocketList[rI].HP - damage

  if(rocketList[rI].HP <= 0):
    print("\n{0} has fainted!".format(rocketList[rI].name))
    if(rI == 2):
      print("\nTeam Rocket has no more usable pokemon, Team {0} is the victor!".format(name))
      exit(0)
    else: 
      rockMove = [0, 0, 0, 0, 0]
      rI = rI + 1
      print("\nTeam Rocket sends out {0}!".format(rocketList[rI].name))