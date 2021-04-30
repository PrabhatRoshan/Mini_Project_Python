# Importing Libraries
# Importing random module which contains a variety of things to do with random number Generation

import random
        
# Importing math module to use in our program as we will use sqrt function later.

import math

# Taking Inputs as lower bound and upper bound for user input

low_bound = int(input("Enter the Lower bound for guessing:- "))

upp_bound = int(input("Enter the Upper bound for guessing:- "))

# Generating a random number between the lower bound and upper bound

rand_num = random.randint(low_bound, upp_bound)

print("\n\tYou will have only ",
      round(math.sqrt(upp_bound - low_bound + 2)),
      " chances to predict the correct number!\n")

# Initializing the number of prediction.

count = 0

# for calculation of minimum number of prediction depends upon range

while count < math.sqrt(upp_bound - low_bound + 2):
    count += 1

    # taking predicted number as input

    predicted_number = int(input("Predict a number:- "))

    # Condition testing

    if rand_num == predicted_number:
        print("Congratulations you did it in ",
              count, " try")

        # Once predicted, loop will break
        break
    elif rand_num > predicted_number:
        print("Your Predicted Number is smaller than the correct conclusion!")
    elif rand_num < predicted_number:
        print("Your Predicted Number is Greater than the correct conclusion!")

# If the number of prediction is more than the range, shows this output.

if count >= math.sqrt(upp_bound - low_bound + 2):
    print("\nThe number is %d" % rand_num)
    print("\tBetter Luck Next time!")