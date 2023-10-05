print("a basic rpg.")
print("you have a few options, you can start or exit.")
start_1 = input("1 to start, anything else to stop: ")
if start_1 == "1":
  with open("class.py") as f:
    exec(f.read())
else:
  print("stopping program")
  