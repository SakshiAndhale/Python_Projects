"""import random

def guess(x):
        random_number = random.randint(1,x)
        #once the comp has generated a random number we have to guess what it might be. The computer will then provide hints if the number is higher or lower than the actual comp generated one.
        guess = 0
        while guess != random_number:
                guess = int(input('Guess a number between 1 and (x): '))
                if guess < random_number:
                        print('Sorry, Guess again. Too Low.')
                elif guess > random_number:
                        print('Too High buddy!')
                
        print('Spot on! You have guessed the number correctly.')"""

"""import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Too high, buddy!')
            
    print('Spot on! You\'ve guessed the number correctly.')

if __name__ == "__main__":
    x = int(input("Enter the upper bound for the guessing game: "))
    guess(x)"""

import random

def main():
    try:
        # Generate a random number between 1 and 100
        random_number = random.randint(1, 100)
        print("A random number between 1 and 100 has been generated.")
        
        # Prompt the user to guess the number
        guess = int(input("Enter your guess: "))
        
        # Verify if the guess is correct
        if guess == random_number:
            print("Congratulations! Your guess is correct.")
        else:
            print(f"Sorry, that's incorrect. The correct number was {random_number}.")
    
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()


