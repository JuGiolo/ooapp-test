"""
    =========== Exercise 1 =============
    I have provided some starter code below
    that creates a result variable, and a number_1
    variable. Your goal is to make number_1 equal 11
    after the operations that have been done to it.
"""

"""
result = 0
number_1 = 5
number_1 += 52
number_1 -= 46
# Do more operations on number 1 until it equals eleven
result = number_1
print(result == 11)

"""

"""
    =========== Exercise 2 =============
    Take input from the command line, and convert it to
    an int. Now pick a range (i.e. 0-10), and create a set
    of conditional statements that prints the string
    representation of the number input by the user.
    For example if someone put in 8, then it would print 'eight'.
    Hint: Use if, elif and else statements.
"""

user_value = int(input("Enter a number between 0 and 10: "))

if user_value == 0:
    print("Zero")
elif user_value == 1:
    print("One")
elif user_value == 2:
    print("Two")
elif user_value == 3:
    print("Three")
elif user_value == 4:
    print("Four")
elif user_value == 5:
    print("Five")
elif user_value == 6:
    print("six")
elif user_value == 7:
    print("seven")
elif user_value == 8:
    print("eight")
elif user_value == 9:
    print("nine")
elif user_value == 10:
    print("ten")
else: # If value is not between 0 and 10
    print("Value provided is not between 0 and 10!")