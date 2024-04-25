#Task 1 Code Correction

place = str(input("Choose a place: forest or cave?"))

if place == "forest":
    action = str(input("climb a tree or cross a river?"))
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
else:
    print("You find a hidden treasure!")

#Task 2 Setting the Scene

if place == "forest":
    action = str(input("climb a tree or cross a river?"))
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place =="cave":
     print("You find a hidden treasure!")
     light = input(str("Would you like to light a torch, or proceed in the dark?"))
     if light =="light a torch":
        print("The gold glitters in the light.")
     else:
         print("Without a light you can't see the gold that is on the cave floor.")
else:
    #Task 3
    pass
    

