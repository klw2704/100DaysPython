# LOOPS

# For Loop
    # for item in list_of_items:
        # do something to that item


fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits: # taking this list of fruits, and assigning a variable name - fruit - to each of them. 
    print(fruit)
    print(fruit + " Pie")


# For Loops and the range() function - useful if you want to generate a range of numbers to loop through
for number in range(1, 11, 3): # this is from 1 to 10, typing 1 to 10 doesn't include 10. The third number is the step size (3 would return 1, 4, 7, 10)
    print(number)


total = 0 # this is our accumulator
for number in range(1, 101):
    total += number
print(total)