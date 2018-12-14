import random, time
assetattack = 0
enemyattack = 0
moneyperturn = 0
money = 1
stage = 0
playing = True
turn = True
enemymt = 1
fighters = 0
alevel = 5

def shell():
  global turn
  global money
  newmine = input("Buy Miners? Y/N")
  newmine = newmine.lower()
  if newmine == "y":
    howmine = input("How many? 1 = $1. ")
    if howmine.isdigit():
      howmine = int(howmine)
      if miner.add(howmine):
        print("$"+str(money))
      else:
        print("Insufficient Funds.")
    else:
      print("Try a digit next time.")
  pass
  newfite = input("Buy Fighters? Y/N")
  newfite = newfite.lower()
  if newfite == "y":
    howfite = input("How many? 1 = $1. ")
    if howfite.isdigit():
      howfite = int(howfite)
      if asset.add(howfite):
        print("$"+str(money))
      else:
        print("Insufficient Funds.")
    else:
      print("Try a digit next time.")
  nexturn = input("Move to next turn? Y/N")
  nexturn = nexturn.lower()
  if nexturn == "y":
    turn = False
  pass

class enemy():
  def add(st):
    global enemyattack
    enemyattack += st
    
class asset():
  def add(invested):
    global money
    global assetattack
    global fighters
    global alevel
    if money >= invested:
      money -= invested
      fighters += invested * alevel
      return True
    else:
      return False

class miner():
  def add(invested):
    global money
    global moneyperturn
    if money >= invested:
      money -= invested
      moneyperturn += invested
      return True
    else:
      return False

while playing:
  stage += 1
  for x in range(1, 6):
    enemy.add(enemymt)
    print(str(6-x)+" from a wave.")
    money += moneyperturn
    print("$" +str(money))
    print(str(moneyperturn)+" Miners")
    print(str(fighters)+" Warriors")
    turn = True
    while turn:
      shell()
  print("Enemy Wave!")
  print("Enemies had "+str(enemyattack))
  print("You had "+str(assetattack))
  assetattac = assetattack - enemyattack
  if assetattac <0:
    playing = False
    print("Game Over")
  else:
    enemyattack -=assetattack
    if enemyattack < 0:
      enemyattack = 0
    print("You won this battle.")
  assetattack = assetattac
  r = assetattack % alevel
  assetattack -= r
  fighters = assetattack / alevel
  time.sleep(2)
  enemymt *= 15
