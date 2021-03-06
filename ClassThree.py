"""
sum = 5 + 3
sum_2 = 2 + sum 
sum_3 = sum + sum_2

my_list = (1,2,3,4)
my_list_2 = (5,6,7,8)
my_list_3 = my_list + my_list_2

my_list_4 = (sum, sum_2, sum_3, "First", "next", "last")


print(type(sum))
# Use the command above to specify the type of language)

print(sum + sum_2)


my_list = [1,2,3,4] # Initialize my_list

my_list = my_list * 3 # Take my_list and multiply it by 3

print(my_list) # Prints: [1,2,3,4,1,2,3,4,1,2,3,4]

print(5 // 3) # Prints: 1


print(5 > 3) # Prints: True; since 5 is greater than 3

result = 5 > 3 # You can store the result in a variable

print(result) # Prints: True

print(3 > 5) # Prints: False; since 3 is NOT greater than 5

print(5 > 5) # Prints: False; since 5 is NOT greater than 5 (they are equal)

x = 2 # Setting up the x variable

if x < 3:
    x += 2 # This will run if x < 3, otherwise it will be skipped over

print(x) # Since this is on a lower indentation level, this code will run regardless

if x < 3:
    x += 2 # This will run if x < 3, otherwise it will be skipped over

print(x) # Since this is on a lower indentation level, this code will run regardless


x = 2 # Setting up the x variable

if x < 3:
    x += 2 # This will run if x < 3, otherwise it will be skipped over
else:
    x -= 1 # This will run if x is not less than 3

print(x) # Since this is on a lower indentation level, this code will run regardless

if x < 3:
    x += 2 # This will run if x < 3, otherwise it will be skipped over
else:
    x -= 1 # This will run if x is not less than 3

print(x) # Since this is on a lower indentation level, this code will run regardless


user_value = int(input("Enter a number between 0 and 5: "))

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
else: # If value is not between 0 and 5
    print("Value provided is not between 0 and 5!")
"""
name = input("Enter name: ") # Take someones name from the command line

print("john" in name) # Prints: True if john is name given, or False otherwise