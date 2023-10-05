from game_loop import gameloop_1

print(".")
print("..")
print("...")
print("(you feel something tapping you)")
print("Hello? Are you alive?")
print("Huh, guess not.")
print("whoever was talking to you has walked awaY.")
print("you can get up noW.")
print("you stand up and see a ball of light in front of you")
print("i am your guide ?@$* you can call me de thougH.")
print("i give you your options seeing as you have no influence in this worlD.")
player_name = input("whats your namE?: ") 
print("Nice to meet you " + player_name)
print("anyway, you have 6 options at the momenT.")
print("you can either move north, south, east, or wesT.")
print("or you can CAMP or CHECK.")
print("CAMP will allow you to recover health at the loss of timE.")
print("CHECK however, will allow you to see your inventory and any status anomalies.")
player_movement = True
while player_movement:
  player_move_choice = input("awnser herE: ")
    
  if player_move_choice == "north":
    print("moving nortH.")
    exec(gameloop_1)
  if player_move_choice == "east":
    print("")
  if player_move_choice == "south":
    print("")
  if player_move_choice == "west":
    print("")
  if player_move_choice == "camp":
    print("")
  if player_move_choice == "check":
    print("")
  else: 
    pass
    