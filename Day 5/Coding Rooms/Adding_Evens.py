total = 0 # this is our accumulator
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

# OR

total2 = 0
for number in range(2, 101, 2):
    total2 += number
print(total2)