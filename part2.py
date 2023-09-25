import dice
import random


def display_details():
    print("File : wayby001_poker.py")
    print("Author : Batman")
    print("Stud_ID : 0123456X")
    print("Email_ID : wayby001")
    print("This is my own work as defined by the")
    print("Universitys Academic Misconduct Policy.")


def roll_die():
    return random.randint(1, 6)


def deal_hand(max_dice):
    hand = []
    i = 0
    while i < max_dice:
        hand.append(roll_die())
        i += 1
    return hand


def rank_hand(hand):
    die_count = [0, 0, 0, 0, 0, 0, 0]
    for i in hand:
        die_count[i] += 1
    rank = 0
    if 5 in die_count:
        rank = 6
    elif 4 in die_count:
        rank = 5
    elif 3 in die_count and 2 in die_count:
        rank = 4
    elif 3 in die_count:
        rank = 3
    elif 2 in die_count:
        rank = 2
    elif 1 in die_count:
        rank = 1
    else:
        rank = 0
    return rank


def display_rank(rank):
    rank_names = {
        0: "Nothing special",
        1: "One pair",
        2: "Two pairs",
        3: "Three of a kind",
        4: "Full house",
        5: "Four of a kind",
        6: "Five of a kind ",
    }
    print(rank_names[rank])


Game_status = True
match_played = 0
Lose = 0
Won = 0
Draw = 0
player_status = [0, 0, 0, 0, 0, 0, 0]


display_details()
while True:
    choice = input("Would you like to play dice poker [y|n]? ").lower()
    if choice == "n":
        print("No worries... another time perhaps... :)")
        exit()
    elif choice == "y":
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
while Game_status == True:
    player_hand = deal_hand(5)
    match_played += 1
    print("players hand:")
    dice.display_hand(player_hand)
    dealers_hand = deal_hand(5)
    print("Dealers hand:")
    dice.display_hand(dealers_hand)

    player_rank = rank_hand(player_hand)
    player_status[player_rank] += 1
    dealer_rank = rank_hand(dealers_hand)

    print("Player has ", end="")
    display_rank(player_rank)
    print("Dealer has ", end="")
    display_rank(dealer_rank)

    if player_rank < dealer_rank:
        print("** Dealer wins! **")
        Lose += 1
    elif player_rank > dealer_rank:
        print("** Player wins! **")
        Won += 1
    else:
        print("** Draw **")
        Draw += 1
    next_game = input("Play again [y|n]? ").lower()
    while next_game != "y" and next_game != "n":
        print("Please enter either 'y' or 'n'.")
        next_game = input("Play again [y|n]? ").lower()
        if next_game == "y":
            break
    if next_game == "n":
        Game_status = False

print()
print("Thanku for playing")
print("Game Summary")
print("============")
print(f"You played {match_played} games")
print("|--> Games won:", Won)
print("|--> Games lost:", Lose)
print("|--> Games drawn:", Draw)
rank_names = {
    0: "Nothing special",
    1: "One pair",
    2: "Two pairs",
    3: "Three of a kind",
    4: "Full house",
    5: "Four of a kind",
    6: "Five of a kind ",
}
print()
print("Hand Stats:")
print("-----------")
i = 0
while i < len(player_status):
    print(rank_names[i], end=": ")
    f = 0
    while f < player_status[i]:
        print("*", end="")
        f += 1
    print()
    i += 1
exit()
