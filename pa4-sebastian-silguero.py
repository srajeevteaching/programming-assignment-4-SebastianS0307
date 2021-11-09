# Programmers: Sebastian Silguero
# Course: CS151, Dr. Rajeev
# Date: Thursday November 4th, 2021
# Program Inputs:
# Program Outputs:

# Importing random module
import random

# Universally declaring the deck throughout the program
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
dealer_hand = []
player_hand = []


def deal_cards(deck):
	dealer = []
	for i in range(15):
		random.shuffle(deck)
		card = deck.pop()
		if card == 1 or 14:
			card = "A"
		elif card == 11:
			card = "J"
		elif card == 12:
			card = "Q"
		elif card == 13:
			card = "K"
		dealer.append(card)
	return dealer


while len(dealer_hand) != 2:
	dealer_hand.append(random.randint(1, 11))
	if len(dealer_hand) == 2:
		print("Dealer has X and", dealer_hand[1])


while len(player_hand) != 2:
	player_hand.append(random.randint(1,11))
	if len(player_hand) == 2:
		print("You have ", player_hand)


if sum(dealer_hand) == 21:
	print("Dealer has BLACKJACK")
	print("Dealer Wins")
elif sum(dealer_hand) > 21:
	print("Dealer has Busted")
	print("You Win")

while sum(player_hand) < 21:
	next_move = str(input("Would you like to hit or stand? > "))
	next_move = next_move.strip().lower()
	if next_move == "hit":
		player_hand.append(random.randint(1, 11))
		print("You have " + str(sum(player_hand)) + " along with ", player_hand)
	elif next_move == "stand":
		print("The dealer has " + str(sum(dealer_hand)) + " along with ", dealer_hand)
		print("You have " + str(sum(player_hand)) + " along with ", player_hand)

		if sum(dealer_hand) > sum(player_hand):
			print("Dealer wins")
		else:
			print("You win")
			break

while sum(dealer_hand) <= 17:
	dealer_hand.append(random.randint(1, 11))

if sum(player_hand) > 21:
	print("You have BUSTED")
	print("Dealer wins")
elif sum(player_hand) == 21:
	print("You have BLACKJACK")
	print("You Win")












