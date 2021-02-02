user_value = (input("Are you a woman? Yes or No > "))
if user_value == 'Yes':
    print("Do you have a degree? Yes = 1  No = 2. >")

elif user_value == 'No':
    print("This is a research for women only. \nThank you for your time!")

else: # If value is not yes or no
    print("Please, note that this is a Yes or No question.\nThank you")
