import random

# Assign constant values
SUITS = ['♠', '♥', '♦', '♣']
NUMBER_CARD = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
FACE_CARD = ['J', 'Q', 'K', 'A']

def random_deck():
    """Generates and returns a shuffled blackjack deck"""
    deck = []
    cards = NUMBER_CARD + FACE_CARD
    
    for suit in SUITS:
        for card in cards:
            deck.append(f"{card}{suit}")
    random.shuffle(deck)
    return deck
        
def score_logic(hand):
    """Calculates the total score of a given hand"""
    score = 0
    ace_count = 0

    for card in hand:
        value = card[:-1]
        if value in ['J', 'Q', 'K']:
            score += 10
        elif value == 'A':
            score += 11
            ace_count += 1
        else:
            score += int(value)
    
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    
    return score

def player_hand(deck):
    """Deals the initial hand for the player"""
    hand = [deck.pop(), deck.pop()]
    return hand

def dealer_hand(deck):
    """Deals the initial hand for the dealer"""
    hand = [deck.pop(), deck.pop()]
    return hand

def hit(deck, hand):
    """Handle players new card requirement"""
    card = deck.pop()
    hand.append(card)
    return card

def stand():
    """Indicates the player wants to stand"""
    pass

def display_gameplay(player, dealer, hide_dealer_card = True):
    print("\n" + "-"  * 30)
    if hide_dealer_card:
        print(f"Dealer's Hand: ['{dealer[0]}', '???']")
    else:
        print(f"Dealer's Hand: {dealer} (Score: {score_logic(dealer)})")
        
    print(f"Your Hand:     {player} (Score: {score_logic(player)})")        
    print("-"  * 30 + "\n")

def main():
    print("Welcome to Blackjack!")
    deck = random_deck()
    
    player_cards = player_hand(deck)
    dealer_cards = dealer_hand(deck)
    
    player_score = score_logic(player_cards)
    
    if player_score == 21:
        print("Blackjack! You win!")
        return
        
    # Player's turn
    while True:
        display_gameplay(player_cards, dealer_cards, hide_dealer_card=True)
        player_score = score_logic(player_cards)
        
        if player_score > 21:
            display_gameplay(player_cards, dealer_cards, hide_dealer_card=False)
            print("Bust! You went over 21. Dealer wins")
            return
            
        choice = input("Do you want to (H)it or (S)tand? ").strip().upper()
        if choice in ['H', 'HIT']:
            drawn_card = hit(deck, player_cards)
            print(f"You hit and drew: {drawn_card}")
        elif choice in ['S', 'STAND']:
            stand()
            print("You decided to stand.")
            break
        else:
            print("Invalid input. Please enter 'H' or 'S'")
            
    # Dealer's turn
    player_score = score_logic(player_cards)
    if player_score <= 21:
        print("\n--- Dealer's Turn ---")
        display_gameplay(player_cards, dealer_cards, hide_dealer_card=False)
        
        dealer_score = score_logic(dealer_cards)
        while dealer_score < 17:
            print("Dealer hits...")
            drawn_card = hit(deck, dealer_cards)
            print(f"Dealer drew: {drawn_card}")
            dealer_score = score_logic(dealer_cards)
            display_gameplay(player_cards, dealer_cards, hide_dealer_card=False)
            
        if dealer_score > 21:
            print("Dealer busts! You win!")
        elif dealer_score > player_score:
            print("Dealer wins!")
        elif dealer_score < player_score:
            print("You win!")
        else:
            print("It's a tie (Push)!")

if __name__ == "__main__":
    main()
