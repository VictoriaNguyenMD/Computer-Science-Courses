import random as rand

suits = ["S", "C", "H", "D"]
rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
def get_card():
    return rand.choice(rank) + rand.choice(suits)

def get_hand():
    return [get_card() for _ in range(5)]

def print_hand(hand):
    for i, card in enumerate(hand):
        print(str(i+1) + ": " + card)

def get_cards_to_replace():
    result = [-1]
    try:
        str_to_replace = input("Enter the positions of the cards you want to replace, separated by commas, or hit enter.\n")
        str_to_replace = "".join(str_to_replace.split())
        if str_to_replace:
            result = list(map(int, str_to_replace.split(",")))
        else:
            result = []
    except ValueError:
        print("Sorry, I didn't understand that! Try again.")
    return result

def get_ranks(hand):
    ranks = [rank.index(card[:-1]) for card in hand]
    ranks.sort(reverse=True)
    return ranks

def decide_winner(hand, dealer_hand):
    player_high_cards = get_ranks(hand)
    dealer_high_cards = get_ranks(dealer_hand)
    for check_fn in check_fns:
        if check_fn(hand):
            if not check_fn(dealer_hand):
                return "player"
            else:
                return "player" if player_high_cards > dealer_high_cards else "dealer"
    if player_high_cards > dealer_high_cards:
        return "player"
    elif dealer_high_cards > player_high_cards:
        return "dealer"
    else:
        return "tie"
    
def poker():
    hand = get_hand()
    dealer_hand = get_hand()
    print("Your hand is:")
    print_hand(hand)
    arr_to_replace = [-1]
    while arr_to_replace and not all(1 <= i <= 5 for i in arr_to_replace):
        arr_to_replace = get_cards_to_replace()
    for i in arr_to_replace:
        hand[i-1] = get_card()
    print("Your new hand is:")
    print_hand(hand)
    print("The dealer's hand is:")
    print_hand(dealer_hand)
    winner = decide_winner(hand, dealer_hand)
    if winner == "player":
        print("Congratulations! You win!")
    elif winner == "dealer":
        print("Oh no! The dealer won this round.")
    else:
        print("It's a tie!")

def get_value(card):
    return card[:-1]

def get_suit(card):
    return card[-1:]
    
def get_numeric_value(card):
    return rank.index(card[:-1]) + 2
    
# ---------------------------------------------
# You don't need to change anything above here.
# ---------------------------------------------

def is_pair(hand): #Check 1 pair
    new_hand = [get_numeric_value(hand[i]) for i in range(len(hand))]
    
    for i in new_hand:
        count = 0
        for check in new_hand:
            if i == check:
                count += 1
            if count == 2:
                return True
    
    return False

def is_two_pairs(hand): #Check 2 pairs
    new_hand = [get_numeric_value(hand[i]) for i in range(len(hand))]
    
    print(new_hand)
    count = 0
    
    for i in range(len(new_hand)):
        for check in range(i + 1, len(new_hand)):
            if new_hand[i] == new_hand[check]:
                count +=1
    print(count)    
    if count == 2:
        return True
    
    return False

def is_three_of_a_kind(hand):
    new_hand = [get_numeric_value(hand[i]) for i in range(len(hand))]
    
    for i in new_hand:
        count = 0
        for check in new_hand:
            if i == check:
                count += 1
            if count == 3:
                return True
    
    return False

def is_straight(hand): #values are consecutive
    new_hand = [get_numeric_value(hand[i]) for i in range(len(hand))]
    new_hand.sort()
    
    answer = True

    for i in range(len(new_hand) - 1):
        if(new_hand[i] + 1 != new_hand[i+1]):
            answer = False
            break
        
    return answer

def is_flush(hand): #suites are the same
    answer = True
    
    for i in range(len(hand) - 1):
        if(get_suit(hand[i]) != get_suit(hand[i+1])):
            answer = False
            break
    
    return answer

def is_full_house(hand):
    new_hand = [get_numeric_value(hand[i]) for i in range(len(hand))]
    
    temp_list = list(set(new_hand))
    
    first = new_hand.count(temp_list[0])
    second = new_hand.count(temp_list[1])
    
    if len(temp_list) == 2:
        if first == 2 or first == 3 and second == 2 or second == 3:
            return True
        
    return False
    
    

def is_four_of_a_kind(hand): #Prints 4 of a kind
    new_hand = [get_numeric_value(hand[i]) for i in range(len(hand))]
    
    for i in new_hand:
        count = 0
        for check in new_hand:
            if i == check:
                count += 1
            if count == 4:
                return True
    
    return False

def is_straight_flush(hand):
    answer = True
    
    if is_straight(hand) == False or is_flush(hand) == False:
        answer = False
    
    return answer

# ---------------------------------------------
# You don't need to change anything below here.
# ---------------------------------------------
check_fns = [is_straight_flush, is_four_of_a_kind, is_full_house, is_straight, is_flush, is_three_of_a_kind, is_two_pairs, is_pair]

if __name__ == "__main__":
    # poker()
    assert is_full_house(["5D", "5C", "5H", "3C", "3S"])
    assert is_full_house(["10D", "4C", "10H", "4C", "10S"])
    
    assert not is_full_house(["5D", "4C", "5H", "3C", "3S"])