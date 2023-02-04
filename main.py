import time
import os
import random
Insane_juggernaut = 1000;
attack = 65;
healing_potion = 0;
Mega_Jump = 90;
Infernal_Barbarian = 1100;
Infernal_Attack = 84;
Infernal_Spin = 88


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
  healing_potion += 1
  print("Attack =")
  print(attack)
  print( )
  print("Your Health =")
  print(Insane_juggernaut)
  print( )
  print("How much healing potion u have")
  print(healing_potion)
  
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
print(1)
os.system('clear')

def moves(choice,attack,Infernal_Attack,Infernal_Spin,Infernal_Barbarian,Insane_juggernaut,Mega_Jump):
  if( choice == "1"):
    print("")
  while(True):
    while(Insane_juggernaut > 0 and Infernal_Barbarian > 0):
      choice1 = input("what attack u wanna do?")
      if(choice1 == "1"):
        Infernal_Barbarian -= attack;
        print( "")
        print("Infernal_barbarian Heath =")
        print(Infernal_Barbarian)
        print("" )
        situationv21 = random.randrange(1,2)
        if(situationv21 == 1):
            Insane_juggernaut -= Infernal_Attack
        elif(situationv21 == 2):
            Insane_juggernaut -= Infernal_Spin
        elif(situationv21 == 2):
          print("Hey He used Infernal_Attack on you")
        elif(situationv21 == 1):
          print("Hey he used Infernal_Attack on you")
        print( )
        print("Your Health =")
        print(Insane_juggernaut)
      break;
    elif(choice1 == "2"):
        Infernal_Barbarian -= Mega_Jump;
        print( )
        print("Infernal_barbarian Heath =")
        print(Infernal_Barbarian)
        print( )
        situationv21 = random.randrange(1,2)
        if(situationv21 == 1):
            Insane_juggernaut -= Infernal_Attack
        elif(situationv21 == 2):
            Insane_juggernaut -= Infernal_Spin
       elif(situationv21 == 2):
          print("Hey He used Infernal_Attack on you")
       elif(situationv21 == 1):
         print("Hey he used Infernal_Attack on you")
       print( )
       print("Your Health =")
       print(Insane_juggernaut)
      break;
print( )
print("y = yes n = no")
xyz = input("Are you ready?")
if(xyz == "y"):
  print("starting")
  os.system('clear')
if(xyz == "n"):
  print("stoping game")
  raise SystemExit
moves(xyz,attack,Infernal_Attack,Infernal_Spin,Infernal_Barbarian,Insane_juggernaut,Mega_Jump)