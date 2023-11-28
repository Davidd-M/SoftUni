import random

tries = 0
difficulty = ValueError  # Easy, Medium or High

while difficulty == ValueError:  # ask for correct input for difficulty
    difficulty = input("Choose difficulty (E for Easy, M for Medium, H for Hard): ").lower()
    if difficulty == 'e':
        tries = 15
    elif difficulty == 'm':
        tries = 10
    elif difficulty == 'h':
        tries = 5
    else:
        difficulty = ValueError

computer_number = random.randint(1, 100)

while tries > 0:
    player_input = input("Guess the number (1 - 100): ")
    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue
    player_number = int(player_input)

    if player_number == computer_number:
        print("You guessed it!")
        break
    elif player_number > computer_number:
        print("Too high!")
    else:
        print("Too low!")
    tries -= 1
    print(f"Tries left: {tries}")

else:  # if the player ran out of tries
    print("Game over!")