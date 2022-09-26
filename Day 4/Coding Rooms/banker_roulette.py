# import random

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# # Get the total number of items in list
# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)
# payer = names[random_choice]
# print(f"{payer} is going to buy the meal today!")




def solution(S):
    # write your code in Python 3.6

    # S = "4 5 6 - 7 +"

    action = S.split(" ")
    print(action)
    result = []
    
    for x in action:
        if (x == '-'):
            result.append(abs(result[-1] - result[-2]))
        elif (x == '+'):            
            result.append(abs(result[-1] - result[-2]))
        elif ("POP"):
            result.pop(result[-1])
        elif ("DUP"):
            result.append(result[-1])
        else:
            result.append(x)

    return result[-1]

print(solution("4 5 6 7 8"))