# Programmers: Jonathan and Sebastian
# Course: CS151, Dr. Rajeev
# Programming Assignment: 4
# Program Inputs: Decision to draw another card or stay with given cards
# Program Outputs: Game outcome, deciding which player wins the round

import random


# Functions creates the list with values from 1 to 14 along with a letter marking the type of card
def generate_card_list(card_type):
    temp_list = []
    for i in range(1, 14):
        temp_list.append(str(i) + card_type)
    return temp_list


# Function replaces the single letter with a complete statement describing the type of card
def str_cards_type(card_list, replace_letter, replace_message):
    card_type_list = []
    for i in card_list:
        new_string = i.replace(replace_letter, replace_message)
        card_type_list.append(new_string)
    return card_type_list


# Replaces the first cards with a number 1 to say ace
def ace_replace(card_list):
    ace_string = card_list[0].replace("1", "ace")
    card_list.insert(0, ace_string)
    card_list.pop(1)
    return card_list


# Takes a card from the generated list of all cards and adds it into the chosen players list
def draw_cards(card_list, player_list, number_of_cards):
    i = 0
    while i < number_of_cards:
        player_list.append(card_list[i])
        i += 1
    for i in range(number_of_cards):
        card_list.pop(0)
    return player_list


# Used to validate if the user input is a digit and if inputted digit is either a 1 or 2
def validate_input(message):
    is_valid = False
    return_message = None
    while not is_valid:
        choice = input(message)
        while not choice.isdigit():
            choice = input(message)
        choice = int(choice)
        is_valid = choice in range(1, 3)
        return_message = choice
    return return_message


# Determines the amount of points the player's hand is worth depending on their cards
def find_points(players_cards):
    total_points = 0
    for i in range(len(players_cards)):
        current_card = players_cards[i]
        if current_card[0] == "k" or current_card[0] == "q" or current_card[0] == "j":
            total_points += 10
        elif current_card[0] == "a":
            ace_choice = validate_input("What will this card be worth? 1 = one point, 2 = eleven points: ")
            if ace_choice == 1:
                total_points += 1
            elif ace_choice == 2:
                total_points += 11
        elif current_card[0] == "1":
            total_points += 10
        else:
            points = int(current_card[0])
            total_points += points
    return total_points


# Determines the amount of points the dealer's hand is worth depending on its cards
def find_dealer_points(dealers_cards):
    total_points = 0
    for i in range(len(dealers_cards)):
        current_card = dealers_cards[i]
        if current_card[0] == "k" or current_card[0] == "q" or current_card[0] == "j":
            total_points += 10
        elif current_card[0] == "a":
            total_points += 11
        elif current_card[0] == "1":
            total_points += 10
        else:
            points = int(current_card[0])
            total_points += points
    return total_points


def main():
    # Initializes Lists which will hold cards accordingly
    all_cards = []
    dealer_cards = []
    player_cards = []

    # Creates the lists of cards according to the type of card
    club_cards_13 = ace_replace(str_cards_type(generate_card_list("c"), "c", " of clubs"))
    heart_cards_13 = ace_replace(str_cards_type(generate_card_list("h"), "h", " of hearts"))
    diamond_cards_13 = ace_replace(str_cards_type(generate_card_list("d"), "d", " of diamonds"))
    spade_cards_13 = ace_replace(str_cards_type(generate_card_list("s"), "s", " of spades"))

    # Adds the created lists of cards into one list containing all cards
    all_cards.extend(club_cards_13)
    all_cards.extend(heart_cards_13)
    all_cards.extend(diamond_cards_13)
    all_cards.extend(spade_cards_13)

    # Replaces the values of all the cards with numbers 13, 12, and 11 to their worded counterpart
    all_cards = str_cards_type(all_cards, "13", "king")
    all_cards = str_cards_type(all_cards, "12", "queen")
    all_cards = str_cards_type(all_cards, "11", "jack")

    # Shuffles the list of all cards to create an unknown order of cards
    random.shuffle(all_cards)

    # Starting hand for player
    player_cards = draw_cards(all_cards, player_cards, 2)
    print("Player's cards: ", player_cards)
    player_points = find_points(player_cards)
    print("Player 1 current points: " + str(player_points))

    # Player decides if they would like to draw a card or settle with their current cards
    is_valid = False
    while player_points < 21 and not is_valid:
        hit_card = validate_input("\nWould you like to draw another card? (enter a number: 1 = yes | 2 = no): ")
        if hit_card == 1:
            new_card = all_cards[0]
            all_cards.pop(0)
            player_cards.append(new_card)
            print("Player's cards: ", player_cards)
            player_points = find_points(player_cards)
            print("Player's current points: " + str(player_points))
        elif hit_card == 2:
            print("Player's cards: ", player_cards)
            print("Player's final points: " + str(player_points))
            is_valid = True

    # Checks to see if player has won, busted, or if the dealer should play
    if player_points == 21:
        print("\nPlayer wins! BlackJack!")
        print("Player has " + str(player_points) + " points")
    elif player_points > 21:
        print("\nPlayer has busted! Dealer wins!")
        print("Player has " + str(player_points) + " points")
    elif player_points < 21:
        print("\nDealers Turn!")

        # Starting hand for dealer
        dealer_cards = draw_cards(all_cards, dealer_cards, 2)
        print("Dealers cards: ", dealer_cards)
        dealer_points = find_dealer_points(dealer_cards)
        print("Dealers current points: " + str(dealer_points))

        # If the amount of points dealer has is less than 17 then it will continue to draw
        while dealer_points < 17:
            new_card = all_cards[0]
            all_cards.pop(0)
            dealer_cards.append(new_card)
            print("\nDealers cards: ", dealer_cards)
            dealer_points = find_dealer_points(dealer_cards)
            print("Dealers current points: " + str(dealer_points))

        # Checks to see if dealer has won, busted, tied, or lost in order to determine a winner
        if dealer_points > 21:
            print("\nDealer has busted! Player Wins!")
            print("Player has " + str(player_points) + " points and Dealer has " + str(dealer_points) + " points")
        elif dealer_points == 21:
            print("\nDealer has won! BlackJack!")
            print("Dealer has " + str(dealer_points) + " points and Player has " + str(player_points) + " points")
        elif player_points > dealer_points:
            print("\nPlayer wins!")
            print("Player has " + str(player_points) + " points and Dealer has " + str(dealer_points) + " points")
        elif dealer_points > player_points:
            print("\nDealer wins!")
            print("Dealer has " + str(dealer_points) + " points and Player has " + str(player_points) + " points")
        elif dealer_points == player_points:
            print("\nThis round is a draw!")
            print("Player has " + str(player_points) + " points and Dealer has " + str(dealer_points) + " points")


main()
