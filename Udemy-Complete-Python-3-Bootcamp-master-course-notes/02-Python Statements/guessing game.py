# First, pick a random integer from 1 to 100 using the random module and assign it to a variable

import random

num = random.randint(1,100)

# print an introduction to the game and explain the rules

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

# Create a list to store guesses zero is a good placeholder value. It's useful because it evaluates to "False"

guesses =[0]

# While loop that asks for a valid guess using int(input()) 

while True:

    guess = int(input("I'm thinking of a number between 1 and 100.\n What is the number?"))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS!! Please try again: ')
        continue

# here we compare the player's guess to our number    
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSE IT IN ONLY {len(guesses)} GUESSES!!')
        break

 # if guess is incorrect, add guess to the list 
 # 
    guesses.append(guess)
    print(guesses)

# when testing the first guess, guesses[-2]==0, which evaluates to False
# and brings us down to the second section

    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')