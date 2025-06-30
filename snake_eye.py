
import random
die1 = random.randint(1,6)
die2 = random.randint(1,6)
total = die1 + die2
print(die1, die2)
print(total)
while total != 2:
  print("nope")
  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  total = die1 + die2
  print(die1, die2)
  print(total)
if total == 2:
  print("snake eyes")
else:
  print("error")
