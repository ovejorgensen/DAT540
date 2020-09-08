def RoPaSc(player_1_hand, player_2_hand):
    if player_1_hand == player_2_hand: return "Draw"
    elif player_1_hand == "scissors":
        if player_2_hand == "paper": result = 1
        else: result = 2
    elif player_1_hand == "paper":
        if player_2_hand == "rock": result = 1
        else: result = 2
    else:
        if player_2_hand == "scissors": result = 1
        else: result = 2 

    return "Player %s: wins." % result

def main():
    print("\nPlayer 1, select hand: ")
    p1 = input().lower()
    print("Player 2, select hand: ")
    p2 = input().lower()

    print("\nPlayer 1: %s" % p1)
    print("Player 2: %s" % p2)
    print(RoPaSc(p1, p2))

if __name__ == "__main__":
    main()