import random

print("Goal is to guess the integer the computer picked.\nHint: Try between 1 and 20")

# Generate the random number once
target = random.randint(1, 20)
count = 1

while True:
    i = int(input("Enter an integer: "))
    
    if i == target:
        print("You guessed it correctly on attempt number {}!".format(count))
        break
    else:
        print("Try again!")
        count += 1
