import random


def gameloop_1():
  temp_value = random.randint(1,15)
  if temp_value == 1:
    print("you encountered a chest")
  if temp_value == 2:
    print("you encounter a town")
  if temp_value == 3:
    print("you encounter a camp of explorers")
  else:
    monster_encounter = ['goblin','goblin','skeleton','green_slime','green_slime']
    print('you encountered a ' + random.choice(monster_encounter))
    gameloop_1