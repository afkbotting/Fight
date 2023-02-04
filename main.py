import time
import os
import random
Insane_juggernaut = 1300;
attack = 100;
healing_potion = 0;
Mega_Jump = 120;
Infernal_Barbarian = 1100;
Infernal_Attack = 84;
Infernal_Spin = 88
health_pot = 0;
titan_serum = 0;
instadamage = 1000;

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
print("U are about unlock Mega jump and instadamage attack that is rly op")
print()
titan_serum += 1;
print( )
print("Here Ur health_potion ammount =")
print(health_pot)
print( )
print("Here Ur titan serum ammount =")
print(titan_serum)
print("1 = no 2 = titan serum")
choice2 = input("hey man would like use a item before the boss fight u may need it just to survive?")
if(choice2 == "1"):
  print(" ")
  print("Alright u quit")
elif(choice2 == "2"):
  Insane_juggernaut += 10000;
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
print(1)
os.system('clear')



