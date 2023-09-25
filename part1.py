import dice
import random

# players_hand=[1,2,3,4,5,6]
# dice.display_hand(players_hand)

Game = False
Match_played = 0
Lose = 0
Player = 0
Draw = 0
player_status = [0, 0, 0, 0, 0, 0, 0]
En = True
print("File : wayby001_poker.py")
print("Author : Batman")
print("Stud_ID : 0123456X")
print("Email_ID : wayby001")
print("This is my own work as defined by the")
print("Universitys Academic Misconduct Policy.")
while En == True:
    choice = input("Would you like to play dice poker [y|n]? ").lower()
    if choice == "n":
        print("No worries... another time perhaps... :)")
        En = False
    elif choice == "y":
        En = False
        Game = True
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
while Game == True:
    Match_played += 1
    players_hand = []
    for i in range(5):
        z = random.randint(1, 6)
        players_hand.append(z)
    dealers_hand = []
    for x in range(5):
        y = random.randint(1, 6)
        dealers_hand.append(y)
    print("players hand:")
    dice.display_hand(players_hand)
    print("Dealers hand:")
    dice.display_hand(dealers_hand)

    player_die_count = [0, 0, 0, 0, 0, 0, 0]
    for i in players_hand:
        player_die_count[i] += 1

    dealers_die_count = [0, 0, 0, 0, 0, 0, 0]
    for i in dealers_hand:
        dealers_die_count[i] += 1

    player_rank = 0
    if 5 in player_die_count:
        player_rank = 6
    elif 4 in player_die_count:
        player_rank = 5
    elif 3 in player_die_count and 2 in player_die_count:
        player_rank = 4
    elif 3 in player_die_count:
        player_rank = 3
    elif 2 in player_die_count:
        player_rank = 2
    elif 1 in player_die_count:
        player_rank = 1
    else:
        player_rank = 0
    player_status[player_rank] += 1
    dealer_rank = 0
    if 5 in dealers_die_count:
        dealer_rank = 6
    elif 4 in dealers_die_count:
        dealer_rank = 5
    elif 3 in dealers_die_count and 2 in dealers_die_count:
        dealer_rank = 4
    elif 3 in dealers_die_count:
        dealer_rank = 3
    elif 2 in dealers_die_count:
        dealer_rank = 2
    elif 1 in dealers_die_count:
        dealer_rank = 1
    else:
        dealer_rank = 0
    rank_names = {
        0: "Nothing special",
        1: "One pair",
        2: "Two pairs",
        3: "Three of a kind",
        4: "Full house",
        5: "Four of a kind",
        6: "Five of a kind ",
    }
    print("player rank:", rank_names[player_rank])
    print("Dealer rank:", rank_names[dealer_rank])
    if player_rank < dealer_rank:
        print("** Dealer wins! **")
        Lose += 1
    elif player_rank > dealer_rank:
        print("** Player wins! **")
        Player += 1
    else:
        print("** Draw! **")
        Draw += 1

    next_game = input("Play again [y|n]? ").lower()
    while next_game != "y" and next_game != "n":
        print("Please enter either 'y' or 'n'.")
        next_game = input("Play again [y|n]? ").lower()
    if next_game == "n":
        Game = False
        print("Thanku for playing")
        print("Game Summary")
        print("============")
        print(f"You played {Match_played} games")
        print("|--> Games won:", Player)
        print("|--> Games lost:", Lose)
        print("|--> Games drawn:", Draw)
        i = 0
        print("Hand Stats:")
        print("-----------")
        while i < len(player_status):
            print(rank_names[i], end=": ")
            f = 0
            while f < player_status[i]:
                print("*", end="")
                f += 1
            print()
            i += 1

    
