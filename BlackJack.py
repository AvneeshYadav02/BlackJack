import random
from art import logo

cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]

def dealer():
    '''When called, this function will deal cards to the player and the dealer'''
    if len(player_cards) == 0:
        print(logo)
        player_cards.append(random.choice(cards))
        player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    else:
        player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))

    print(f"\n{name}'s cards: {player_cards} ||| Sum: {sum(player_cards)}")
    print(f"Dealer's Cards: [{dealer_cards[0]}, *]")

def player_turn():
        global rerun, player_sum
        if player_sum == 21:
            print(player_cards)
            print("YOU WIN !!")
            print(f"Your Cards :{player_cards}\nDealer's Cards :{dealer_cards}")
            rerun = False
        elif player_sum > 21:
            print("YOU LOSE !!")
            print(f"Your Cards :{player_cards}\nDealer's Cards :{dealer_cards}")
            rerun = False

def dealer_turn():
        global dealer_sum
        while dealer_sum <= 16:
            dealer_cards.append(random.choice(cards))
            dealer_sum = sum(dealer_cards)

def winner_check():
            global rerun, player_sum, dealer_sum
            if player_sum < 21:
                player_choice = int(input("'1' for Hit, '2' for Stand:\n"))
                if player_choice == 2 and player_sum < dealer_sum and dealer_sum < 21:
                    print("YOU LOSE !!!")
                    print(f"Your Cards :{player_cards}\nDealer's Cards :{dealer_cards}")
                    rerun = False
                elif (player_choice == 2 and player_sum > dealer_sum) or dealer_sum > 21:
                    print("YOU WIN !!")
                    print(f"Your Cards :{player_cards}\nDealer's Cards :{dealer_cards}")
                    rerun = False
                elif player_choice == 2 and player_sum == dealer_sum and player_sum <= 21:
                    print("ITS A TIE !!")
                    print(f"Your Cards :{player_cards}\nDealer's Cards :{dealer_cards}")
                    rerun = False

name = input("WELCOME TO BLACKJACK \nEnter your name:\n")

player_cards = []
dealer_cards = []
rerun = True

while rerun:
    dealer()
    player_sum = sum(player_cards)
    dealer_sum = sum(dealer_cards)
    player_ace_or_not = 21 - player_sum
    dealer_ace_or_not = 21 - dealer_sum

    if (player_cards[-1] == 1) and (11 <= player_ace_or_not <= 21):
        player_cards[-1] = 11
    
    if (dealer_cards[-1] == 1) and (11 <= dealer_ace_or_not <= 21):
        dealer_cards[-1] = 11

    dealer_turn()
    player_turn()
    winner_check()
    if rerun == False:
        player_choice = input("Do you want to play again?'1' for yes, '2' for no:\n")
        if player_choice == 1:
            rerun = True
            player_cards = []
            dealer_cards = []
            print("\n" * 25)
        else:
            print("\n" * 25)      