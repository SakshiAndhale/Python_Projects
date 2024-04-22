print("Welcome to my computer quiz!")

playing = input("Would you  like to start?")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What has keys but can't open locks?")
if answer.lower() == "piano":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What has a head, a tail, but no body?")
if answer.lower() == "coin":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("I'm not alive, but I can die. I have no mouth, but I can scream. What am I? ")
if answer.lower() == "candle":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("The more you have of it, the less you see. What is it? ")
if answer.lower() == "darkness":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("Congratulations! Your Score is:  " + str(score) + " questions correct!")
print("Congratulations! You've got: " + str((score / 4) * 100) + "%.")