gryffindor = 0
ravenclaw = 0
slytherin = 0
hufflepuff = 0
print("THE SORTING HAT")
print("A) do you like dusk or dawn? \n"
      "  1)dusk"
      "  2)dawn")
answer = int(input("enter your answer: "))
if answer == 1:
    gryffindor = gryffindor + 1
    ravenclaw = ravenclaw + 1
elif answer == 2:
    slytherin = slytherin + 1
    hufflepuff = hufflepuff + 1
else:
    print("wrong input")

print("B) When I’m dead, I want people to remember me as: \n"
      "  1)The Good"
      "  2)The Great"
      "  3)The Wise"
      "  4)The Bold")
answer = int(input("enter your answer: "))
if answer == 1:
    hufflepuff += 2
elif answer == 2:
    slytherin += 2
elif answer == 3:
    gryffindor += 2
elif answer == 4:
    ravenclaw += 2
else:
    print("wrong input")

print("C) Which instrument pleases your ears the most?\n"
      "  1)the violin"
      "  2)the trumpet"
      "  3)the piano"
      "  4)the drum")
answer = int(input("enter your answer: "))
if answer == 1:
    hufflepuff += 4
elif answer == 2:
    slytherin += 4
elif answer == 3:
    gryffindor += 4
elif answer == 4:
    ravenclaw += 4
else:
    print("wrong input")

print("Gryffindor: " ,gryffindor)
print("Slytherin: " ,slytherin)
print("Hufflepuff: " ,hufflepuff)
print("Ravenclaw: " ,ravenclaw)

if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
    print("The house with the most points is GRYFFINDOR")
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
    print("The house with the most points is RAVENCLAW")
elif hufflepuff >= slytherin:
    print("The house with the most points is HUFFLEPUFF")
else:
    print("The house with the most points is SLYTHERIN")
