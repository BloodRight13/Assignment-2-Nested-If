#Task 1 Code Correction

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)


#Task 2 Venue Selection

selection = "projector" if attendees <= 100 else "audio system"
print(selection)

#Task 3 Catering Choices

catering = str(input("Would you like vegetarian food?"))
food = "Veggie Delight Caterers" if catering == "yes" else "Gourmet Meal Caterers"
print(food)