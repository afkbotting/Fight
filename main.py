
print("Nice U reach the dungeon")
print( )
import time
import os
import random
#Ur abillity + ur health
Insane_juggernaut = 1300;
attack = 100;
instadamage = 1000;
Mega_Jump = 1000
defeated_mindgames = 10000;
enermous_explosion = 2200
#Infernal_Barbarian stuff
Infernal_Barbarian = 1100;
Infernal_Attack = 84;
Infernal_Spin = 88
#amongus stuff
titan_amongus = 10000;
SUSY_ATTACK = 1600;
Heart_attack = 900;
Poison = 999;
Sending_little_impostorkillers = 800;
#nebula stuff
Nebula_corps = 20000;
Nebula_ball = 2300;
Super_charged_nebula_ball = 2400;
Nebula_exploison = 2300;
Nebula_Superexplosion = 2350;
#babstuff
Bab = 0;
#misc
health_pot = 0;
titan_serum = 0;
Mobkiller = 0;
coins = 0;
#Galactic killer
Galactic_killer = 100000;
mega_ball = 15000;
Mind_games = 15900;

print("welcome to level one")
print( )
situation = random.randrange(1,4)
if(situation == 1):
  print("Nice u got armor")
  Insane_juggernaut += 200;
  print("Attack =")
  print(attack)
  print( )
  print("Your Health =")
  print(Insane_juggernaut)
elif(situation == 2):
  print("Nice u got a really op sword called Infernal rageblade")
  attack += 40
  print("Attack =")
  print(attack)
  print( )
  print("Your Health =")
  print(Insane_juggernaut)
elif(situation == 3):
  print("Oh No u got cursed u loss 150 health")
  Insane_juggernaut -= 150
  print("Attack =")
  print(attack)
  print( )
  print("Your Health =")
  print(Insane_juggernaut)
elif(situation == 4):
  print("Nice u got a really op sword called Infernal rageblade and a healing potion")
  attack += 40
  print("Attack =")
  print(attack)
  print( )
  print("Your Health =")
  print(Insane_juggernaut)
  print( )
  print("How much healing potion u have")
  print(healing_potion)
  
print( )
print("a entity is spawning")
time.sleep(2)
os.system('clear')
print("3")
time.sleep(1)
os.system('clear')
print("2")
time.sleep(1)
os.system('clear')
print(1)
os.system('clear')

while(Insane_juggernaut > 0 and Infernal_Barbarian > 0):
  print("1 equal to use attack")
  choice1 = input("what attack u wanna do?")
  if(choice1 == "1"):
    Infernal_Barbarian -= attack;
    print(" ")
    print("Infernal_barbarian Heath =")
    print(Infernal_Barbarian)
    print(" ")
    situationv21 = random.randrange(1,3)
    if(situationv21 == 1):
      Insane_juggernaut -= Infernal_Attack
      print("Hey He used Infernal_Attack on you")
    elif(situationv21 == 2):
      Insane_juggernaut -= Infernal_Spin
      print("Hey He used Infernal_Spin on you")
    print( )
    print("Your Health =")
    print(Insane_juggernaut)
os.system('clear')  
print("Nice u beat it")
print( )
print("U are about unlock Mega jump and instadamage attack that is rly op and u got more damage on older abillitied")
print()
titan_serum += 1;
print( )
print("Here Ur titan serum ammount =")
print(titan_serum)
print("1 = no 2 = titan serum")
choice2 = input("hey man would like use a item before the boss fight u may need it just to survive?")
if(choice2 == "1"):
  print(" ")
  print("Alright u quit")
elif(choice2 == "2"):
  titan_serum -= 1;
  attack += 900
  Insane_juggernaut += 10000;
  print("How much do attack do =")
  print(attack)
if(Insane_juggernaut < 0):
  print("You Loss Now u gotta press run again")
  raise SystemExit
elif(Insane_juggernaut > 0):
  print("You beated him")
os.system('clear')  
print("Boss fight is about to start Ong")
print( )
print("a boss is spawning")
time.sleep(2)
os.system('clear')
print("3")
time.sleep(1)
os.system('clear')
print("2")
time.sleep(1)
os.system('clear')
print("1")
os.system('clear')

while(Insane_juggernaut > 0 and titan_amongus > 0):
  print("1 = insta damage, 2 = attack, 3 = Mega jump")
  choice3 = input("What u want to do?")
  if(choice3 == "1"):
    titan_amongus -= instadamage;
    print( )
    print("titan_amongus Heath =")
    print(titan_amongus)
    print( )
    situationv22 = random.randrange(1,5)
    if(situationv22 == 1):
      Insane_juggernaut -= SUSY_ATTACK;
      print("He used Susy attack on you")
    elif(situationv22 == 2):
      Insane_juggernaut -= Heart_attack;
      print("He use HeartAttack on you")
    elif(situationv22 == 3):
      Insane_juggernaut -= Poison;
      print("he used poison on you")
    elif(situationv22 == 4):
      Insane_juggernaut -= Sending_little_impostorkillers
      print("He send imposter do damage on you")
    print( )
    print("Your Health =")
    print(Insane_juggernaut)
  elif(choice3 == "2"):
    titan_amongus -= attack;
    print( )
    print("titan_amongus Heath =")
    print(titan_amongus)
    print( )
    situationv22 = random.randrange(1,5)
    if(situationv22 == 1):
      Insane_juggernaut -= SUSY_ATTACK;
      print("He used Susy attack on you")
    elif(situationv22 == 2):
      Insane_juggernaut -= Heart_attack;
      print("He use HeartAttack on you")
    elif(situationv22 == 3):
      Insane_juggernaut -= Poison;
      print("he used poison on you")
    elif(situationv22 == 4):
      Insane_juggernaut -= Sending_little_impostorkillers
      print("He send imposter do damage on you")
    print( )
    print("Your Health =")
    print(Insane_juggernaut)
  elif(choice3 == "3"):
    Insane_juggernaut -= Mega_Jump;
    print( )
    print("titan_amongus Heath =")
    print(titan_amongus)
    print( )
    situationv22 = random.randrange(1,5)
    if(situationv22 == 1):
      Insane_juggernaut -= SUSY_ATTACK;
      print("He used Susy attack on you")
    elif(situationv22 == 2):
      Insane_juggernaut -= Heart_attack;
      print("He use HeartAttack on you")
    elif(situationv22 == 3):
      Insane_juggernaut -= Poison;
      print("he used poison on you")
    elif(situationv22 == 4):
      Insane_juggernaut -= Sending_little_impostorkillers
      print("He send imposter do damage on you")
    print( )
    print("Your Health =")
    print(Insane_juggernaut)
    
os.system('clear')      
if(Insane_juggernaut > 0):
  print("nice u beated it")
else:
  print("U died rip bozo :skull: Imagine being so close but u died")
  raise SystemExit
os.system('clear')
print("U reach level 2 of the dungeon")
print( )
print("U unlocked enermous explosion and u got more damage on older abillited as stated before") 
print( )
Insane_juggernaut += 16999;
print("U got more health you health is =")
print(Insane_juggernaut)
instadamage += 900;
Mega_Jump += 999;
attack += 7000

time.sleep(2)
print("You reach level 2")
print( )
print("level 2 enemy is about to spawn in")
print("3")
time.sleep(1)
os.system('clear')
print("2")
time.sleep(1)
os.system('clear')
print("1")
os.system('clear')

while(Insane_juggernaut > 0 and Nebula_corps > 0):
  print("1 = attack, 2 = enormous explosion, 3 = megajump, 4 = instadmage")
  choice4 = input("what attack u wanna do?")
  if(choice4 == "1"):
    Nebula_corps -= attack;
    print("Nebula_crops health =")
    print(Nebula_corps)
    print( )
    situation69 = random.randrange(1,5)
    if(situation69 == 1):
      Insane_juggernaut -= Nebula_ball;
      print("Boi he used Nebula ballon you")
    elif(situation69 == 2):
      Insane_juggernaut -= Super_charged_nebula_ball;
      print("He used Super charged nebula ballon u")
    elif(situation69 == 3):
      Insane_juggernaut -= Nebula_exploison;
      print("He used Nebula explosion on u")
    elif(situation69 == 4):
      Insane_juggernaut -= Nebula_Superexplosion;
      print("He used super nebula explosion on you")
    print( )
    print("Your health =")
    print(Insane_juggernaut)
  if(choice4 == "2"):
    Nebula_corps -= enermous_explosion;
    print("Nebula_corps health =")
    print(Nebula_corps)
    print( )
    situation69 = random.randrange(1,5)
    if(situation69 == 1):
      Insane_juggernaut -= Nebula_ball;
      print("Boi he used Nebula ballon you")
    elif(situation69 == 2):
      Insane_juggernaut -= Super_charged_nebula_ball;
      print("He used Super charged nebula ballon u")
    elif(situation69 == 3):
      Insane_juggernaut -= Nebula_exploison;
      print("He used Nebula explosion on u")
    elif(situation69 == 4):
      Insane_juggernaut -= Nebula_Superexplosion;
      print("He used super nebula explosion on you")
    print( )
    print("Your health =")
    print(Insane_juggernaut)
  if(choice4 == 3):
    Nebula_corps -= Mega_Jump;
    print("Nebula_crops health =")
    print(Nebula_corps)
    print( )
    situation69 = random.randrange(1,5)
    if(situation69 == 1):
      Insane_juggernaut -= Nebula_ball;
      print("Boi he used Nebula ballon you")
    elif(situation69 == 2):
      Insane_juggernaut -= Super_charged_nebula_ball;
      print("He used Super charged nebula ballon u")
    elif(situation69 == 3):
      Insane_juggernaut -= Nebula_exploison;
      print("He used Nebula explosion on u")
    elif(situation69 == 4):
      Insane_juggernaut -= Nebula_Superexplosion;
      print("He used super nebula explosion on you")
    print( )
    print("Your health =")
    print(Insane_juggernaut)
  if(choice4 == "4"):
    Nebula_corps -= instadamage;
    print("Nebula corps health =")
    print( )
    situation69 = random.randrange(1,5)
    if(situation69 == 1):
      Insane_juggernaut -= Nebula_ball;
      print("Boi he used Nebula ballon you")
    elif(situation69 == 2):
      Insane_juggernaut -= Super_charged_nebula_ball;
      print("He used Super charged nebula ballon u")
    elif(situation69 == 3):
      Insane_juggernaut -= Nebula_exploison;
      print("He used Nebula explosion on u")
    elif(situation69 == 4):
      Insane_juggernaut -= Nebula_Superexplosion;
      print("He used super nebula explosion on you")
    print( )
    print("Your health =")
    print(Insane_juggernaut)
    
os.system('clear')
print("Noice U beated him U can start collecting coins but since this is ur first time U got 2000 coins would like to buy something from Bab")
print( )
print("U got more health")
Insane_juggernaut + 50000;
coins += 2000;
print()
print("Hello Traveler")
print("⠀⣀⣤⡶⠾⠛⠛⠋⠉⠙⠛⠿⠶⣦⣄")
print("⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣦⡀")
print("⣼⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⡄")
print("⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷")
print("⢸⡇⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿")
print("⠘⣿⡀⠀⠀⣰⠟⣭⣿⣽⢷⣴⢟⣽⣯⡙⢷⡀⠀⠀⣸⡇")
print("⠀⠘⢷⣄⠀⣿⠀⠻⠿⠟⢸⣏⠘⠿⠿⠃⢸⡇⢀⣴⠏⠀")
print("⠀⣴⣦⡙⣷⣿⣷⣄⣀⣤⣾⢿⣦⣀⣀⣤⡾⣷⢿⣥⣦⡀")
print("⢸⡯⠀⠹⠿⢇⠌⠉⠋⠉⠁⡀⢉⠙⠛⠉⠸⢿⠟⠁⢸⡇")
print("⠈⢿⣄⡨⠠⠀⣁⡅⠀⠉⠆⡐⠀⠀⢮⣆⠈⠊⠀⢰⣼⠇")
print("⠀⠀⠉⠛⠛⠛⣿⣿⣀⣠⡼⢷⣄⣄⣀⣿⠛⠛⠛⠋⠁⠀")
print("")

while(coins > 0 or Bab < 0):
  print("Nice U reach Bab Shop what U like to buy")
  print("1 = The mobkiller - could remove mobs out exists or 2 = More strength 3 = exits")
  print("Oh forgot about the price The mobkiller is 1k and strength is 2k also")
  print("")
  choice5 = input("what want to do")
  if(choice5 == "1"):
    Mobkiller += 1;
    coins -= 1000;
  if(choice5 == "2"):
    attack += 30000;
    enermous_explosion += 30000;
    Mega_Jump += 30000;
    instadamage += 30000;
  if(choice5 == "3"):
    Bab += 1

print("A boss is spawning at level 2 now")
print("3")
time.sleep(1)
os.system('clear')
print("2")
time.sleep(1)
os.system('clear')
print("1")
os.system('clear')
while(Insane_juggernaut > 0 and Galactic_killer > 0):
  print("1 = attack, 2 = enormous explosion, 3 = megajump, 4 = instadmage 5 = use mobkiller")
  choice6 = input("what would u like to do")
  if(choice6 == "1"):
    Galactic_killer -= attack;
    print("his health =")
    print(Galactic_killer)
    situationpee = random.randrange(1,3)
    if(situationpee == 1):
      Insane_juggernaut -= mega_ball;
      print("He used mega ball to u")
    elif(situationpee == 2):
      situationmindgames = random.randrange(1,3)
    if(situationmindgames == 1):
      mindgames = input("who is attacking u, A = galactic killer, B Ur self")
      if(mindgames == "A"):
        Galactic_killer -= defeated_mindgames;
        print("His health =")
        print(Galactic_killer)
        print("U beat his tricks")
      elif(Mind_games == "B"):
        Insane_juggernaut -= 15900;
        print("U chose the wrong choice")
      elif(mindgames != "A" and mindgames != "B"):
        Insane_juggernaut -= 17000;
        print("U have Not choose a choice so u lose more health")
    print("ur health =")
    print(Insane_juggernaut)
  elif(choice6 == "2"):
    Galactic_killer -= enermous_explosion;
    print("his health =")
    print(Galactic_killer)
    situationpee = random.randrange(1,3)
    if(situationpee == 1):
      Insane_juggernaut -= mega_ball;
      print("He used mega ball to u")
    elif(situationpee == 2):
      situationmindgames = random.randrange(1,3)
    if(situationmindgames == 1):
      mindgames = input("who is attacking u, A = galactic killer, B Ur self")
      if(mindgames == "A"):
        Galactic_killer -= defeated_mindgames;
        print("His health =")
        print(Galactic_killer)
        print("U beat his tricks")
      elif(Mind_games == "B"):
        Insane_juggernaut -= 15900;
        print("U chose the wrong choice")
      elif(mindgames != "A" and mindgames != "B"):
        Insane_juggernaut -= 17000;
        print("U have Not choose a choice so u lose more health")
    print("ur health =")
    print(Insane_juggernaut)
  elif(choice6 == "3"):
    Galactic_killer -= Mega_Jump;
    print("his health =")
    print(Galactic_killer)
    situationpee = random.randrange(1,3)
    if(situationpee == 1):
      Insane_juggernaut -= mega_ball;
      print("He used mega ball to u")
    elif(situationpee == 2):
      situationmindgames = random.randrange(1,3)
    if(situationmindgames == 1):
      mindgames = input("who is attacking u, A = galactic killer, B Ur self")
      if(mindgames == "A"):
        Galactic_killer -= defeated_mindgames;
        print("His health =")
        print(Galactic_killer)
        print("U beat his tricks")
      elif(Mind_games == "B"):
        Insane_juggernaut -= 15900;
        print("U chose the wrong choice")
      elif(mindgames != "A" and mindgames != "B"):
        Insane_juggernaut -= 17000;
        print("U have Not choose a choice so u lose more health")
    print("ur health =")
    print(Insane_juggernaut)
  elif(choice6 == "4"):
    Galactic_killer -= instadamage;
    print("his health =")
    print(Galactic_killer)
    situationpee = random.randrange(1,3)
    if(situationpee == 1):
      Insane_juggernaut -= mega_ball;
      print("He used mega ball to u")
    elif(situationpee == 2):
      situationmindgames = random.randrange(1,3)
    if(situationmindgames == 1):
      mindgames = input("who is attacking u, A = galactic killer, B Ur self")
      if(mindgames == "A"):
        Galactic_killer -= defeated_mindgames;
        print("His health =")
        print(Galactic_killer)
        print("U beat his tricks")
      elif(Mind_games == "B"):
        Insane_juggernaut -= 15900;
        print("U chose the wrong choice")
      elif(mindgames != "A" and mindgames != "B"):
        Insane_juggernaut -= 17000;
        print("U have Not choose a choice so u lose more health")
    print("ur health =")
    print(Insane_juggernaut)
  elif(choice6 == "5"):
    if(Mobkiller > 0):
      Galactic_killer -= Galactic_killer;
      Mobkiller -= 0;
      yes = "how many mob kller u have ="
      print(yes)
      print(Mobkiller)
    elif(Mobkiller == 0):
      print("Sorry U dont have that")

