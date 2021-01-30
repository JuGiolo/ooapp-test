user_value = int(input("Are you a student? Yes = 1  No = 2. "))
if user_value == 1:
    print("What is your name?")
elif user_value == 2:
    print("How old are you")
else: # If value is not yes or no
    print("This is a Yes or No question")