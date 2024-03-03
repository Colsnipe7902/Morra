from random import randint

game_rules = """
    Welcome to Morra! In this game, you'll decide how many fingers
    to hold up (from one hand) and then the computer will randomly
    do the same. You'll need to guess the total number of fingers
    to win the round, before seeing how many fingers the computer
    has decided to hold up! You win when you get to ten.
"""
print(game_rules)

user_score = 0
computer_score = 0

while user_score < 10 and computer_score < 10:
    user_input = int(input("How many fingers do you want to hold up? (Enter a number from 1 to 5): "))
    
    if user_input > 5:
        print("Please type a number from 1 to 5.")
        continue

    user_guess = int(input("How many fingers do you think the computer held up? (Enter a number from 1 to 5): "))
    computer_input = randint(1, 5)
    print(f"The computer holds up {computer_input} fingers.")

    if (user_input + computer_input)  == user_guess :
        print("Good job, you guessed correctly and you got a point.")
        user_score += 1
    else:
        print(f"Sorry, you guessed incorrectly. The computer was holding {computer_input} fingers up.")
        computer_score += 1

    print(f"Your score: {user_score}, Computer's score: {computer_score}\n")

if user_score == 10:
    print("Congratulations! You win!")
else:
    print("Sorry, the computer wins. Better luck next time!")
