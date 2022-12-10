############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/

import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

computer_cards = []
computer_score = 0
while computer_score < 17:
        cc1 = random.choice(cards)
        computer_cards.append(cc1)
        computer_score += cc1

def my_blackjack():

    from art import logo
    print(logo)

    def player_score():
        player_cards = []
        player_score = 0
        while len(player_cards) < 2:
            c1 = random.choice(cards)
            player_cards.append(c1)
            player_score += c1
    
        print(f"Your cards: {player_cards}, current score:{player_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        should_continue = True
        while should_continue:
            if player_score < 21:
                another_card = input("Do you want another card? y or n: ")
                if another_card == "y":
                    c2 = random.choice(cards)
                    player_cards.append(c2)
                    player_score += c2
                    print(f"Your cards: {player_cards}, current score:{player_score}")
                else:
                    should_continue = False
    
            else:
                if 11 in player_cards:
                    for i in range(0,len(player_cards)):
                        if player_cards[i] == 11:
                            player_cards[i] = 1
                else:
                    print("You went over. You lose :(")
                    return
    
        else:
            print(f"Computer's final hand: {computer_cards}, Computer's score: {computer_score}")
            if computer_score > 21:
                print("Computer went over. You win!!")
                return
            elif computer_score > player_score:
                print("You lose :(")
                return
            elif computer_score == player_score:
                print("Its a draw")
                return
            elif computer_score < player_score and player_score == 21:
                print("You win by Blackjack!!")
                return
            elif computer_score < player_score:
                print("You win!!")
                return
            
    player_score()

cont = True
while cont:
    blackjack = input("Do you want a game of blackjack? y or n? ")
    if blackjack == "y":
        my_blackjack()
    else:
        cont = False
else:
    print("Ok np")