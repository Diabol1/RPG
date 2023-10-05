
print("choose a class. you have 3 options, warrior, mage, or none.")
print("you will have a basic stat total of 26p")
print("it will be spread between strength, magic, defense, and vitality.")
print("each class will start with different weapons as well as stat spread.")
print("warriors will have rookie heavy armor along with a rookie sword.")
print("mages will have rookie light armor with a rookie staff")
print("none will have rookie rags with a rookie dagger")
print("warriors will have 9p in strength,3p in magic,7p in vitality,and 7p in defense.")
print("mages will have 3p in strength,11p in magic,6p in vitality,and 6p in defense.")
print("none will have 20p evenly spread between the 4 stats")
player_choice = input("input a class(case sensitive) mage, warrior, or none: ")
if player_choice == "warrior":
  player_strength = 9
  player_magic = 3
  player_vitality = 7
  player_defense = 7
  print("loading world as a warrior")
elif player_choice == "mage":
  player_strength = 3
  player_magic = 11
  player_vitality = 6
  player_defense = 6
  print("loading world as a mage")
else: 
  player_strength = 5
  player_magic = 5
  player_vitality = 5
  player_defense = 5
  print("loading world as a classless, good luck")
with open("world.py") as k:
    exec(k.read())
    