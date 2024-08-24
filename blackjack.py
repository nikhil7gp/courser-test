import random as rn
playerIn = True
dealerIn = True

# card's deck / dealer & player's hands
deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,'J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','A']
player_hand = []
dealer_hand = []

# cards deal
def dealCard(turn):
    card = rn.choice(deck)
    turn.append(card)
    deck.remove(card)
    
# total of each hand cal
def total(turn):
    total = 0
    face = {'J', 'K', 'Q'}
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total +=1
            else:
                total +=11
    return total

# winner validation
def revealDealerHand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]

# rounds (loop)
for _ in range(2):
    dealCard(dealer_hand)
    dealCard(player_hand)

while playerIn or dealerIn:
    print(f"Dealer had {revealDealerHand} and X")
    print(f"You have had {player_hand} for a total of {total(player_hand)}")
    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealer_hand) > 16:
        dealerIn = False;
    else:
        dealCard(dealer_hand)
    if stayOrHit == '1':
        playerIn = False
    else:
        dealCard(player_hand)
    if total(player_hand) >= 21:
        break
    elif total(dealer_hand) >=21:
        break

if total(player_hand) == 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total {total(dealer_hand)}")
    print("Blackjiack! You Win!")
elif total(dealer_hand) == 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total {total(dealer_hand)}")
    print("Blackjiack! Dealer Wins!")
elif total(player_hand) > 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total {total(dealer_hand)}")
    print("You bust! Dealer Wins!")
elif total(dealer_hand) > 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total {total(dealer_hand)}")
    print("Dealer busts! You Win!")
elif 21 - total(dealer_hand) < 21 - total(player_hand):
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total {total(dealer_hand)}")
    print("Dealer Wins!")
elif 21 - total(dealer_hand) > 21 - total(player_hand):
    print(f"\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total {total(dealer_hand)}")
    print("You Wins!")


    
