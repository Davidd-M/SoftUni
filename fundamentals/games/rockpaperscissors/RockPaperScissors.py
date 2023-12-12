import random
from colorama import Fore, Style

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
player_wins = 0
computer_wins = 0
draws = 0

while True:
    player_move = input("Choose [R]ock, [P]aper or [S]cissors: ").lower()
    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        print('Invalid input. Try again...')
        continue

    computer_rand_int = random.randint(1, 3)
    computer_move = ''
    if computer_rand_int == 1:
        computer_move = rock
    elif computer_rand_int == 2:
        computer_move = paper
    else:
        computer_move = scissors
    print(Fore.BLUE + f"The computer chose {computer_move}." + Style.RESET_ALL)
    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print(Fore.GREEN + "You win!" + Style.RESET_ALL)
        player_wins += 1
    elif player_move == computer_move:
        print(Fore.YELLOW + 'Draw!' + Style.RESET_ALL)
        draws += 1
    else:
        print(Fore.RED + 'You lose!' + Style.RESET_ALL)
        computer_wins += 1
    score = (f"Player wins: {Fore.GREEN + str(player_wins) + Style.RESET_ALL} | "
             f"Computer wins: {Fore.RED + str(computer_wins) + Style.RESET_ALL} | "
             f"Draws: {Fore.YELLOW + str(draws) + Style.RESET_ALL}")
    print(score)
    while True:
        game_quit = input("Press [Q]uit to quit or [C]ontinue to continue: ").lower()
        if game_quit == 'q':
            raise SystemExit
        elif game_quit == 'c':
            break
        else:
            print('Invalid input. Try again...')
            continue
    continue
