# Prisoner's Dilemma with user input and choice explanations

def prisoner_dilemma(player_a_choice, player_b_choice):
    if player_a_choice == "cooperate" and player_b_choice == "cooperate":
        return "Both players receive lighter sentences."
    elif player_a_choice == "cooperate" and player_b_choice == "defect":
        return "Player A receives a heavy sentence, and Player B goes free."
    elif player_a_choice == "defect" and player_b_choice == "cooperate":
        return "Player A goes free, and Player B receives a heavy sentence."
    elif player_a_choice == "defect" and player_b_choice == "defect":
        return "Both players receive moderate sentences."

def play_game():
    # Synopsis of the game
    print("==================================================")
    print("Welcome to the Prisoner's Dilemma Game!")
    print("In this game, you and another player are faced with a dilemma.")
    print("You can choose to 'cooperate' and trust the other player, or 'defect' to minimize your own sentence.")
    print("However, your choice also depends on what the other player decides.")
    print("Your goal is to make the best decision for yourself based on the outcomes of cooperation and defection.")
    print("Let's see how the choices play out!\n")

    while True:
        # Get choices from players
        print("==================================================")
        player_a_choice = input("Player A, choose 'cooperate' or 'defect': ").lower()
        player_b_choice = input("Player B, choose 'cooperate' or 'defect': ").lower()
        print("==================================================")

        # Explanations of choices
        explanation_a = "Player A cooperates: Player A is hoping for a lighter sentence by trusting Player B."
        explanation_b = "Player B cooperates: Player B is also hoping for a lighter sentence by trusting Player A."
        explanation_defect_a = "Player A defects: Player A is trying to minimize their own sentence, regardless of Player B's choice."
        explanation_defect_b = "Player B defects: Player B is trying to minimize their own sentence, regardless of Player A's choice."

        # Print explanations
        print("\nExplanations:")
        print("==================================================")
        if player_a_choice == "cooperate":
            print(explanation_a)
        else:
            print(explanation_defect_a)

        if player_b_choice == "cooperate":
            print(explanation_b)
        else:
            print(explanation_defect_b)

        result = prisoner_dilemma(player_a_choice, player_b_choice)
        print("\nOutcome:", result)
        print("==================================================")

        # Ask if the player wants to repeat the game
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again == "no" or play_again == "n":
            print("Thanks for playing!")
            # exit the program
            break
        else:
            print("\n")

# Call the function to start the game
play_game()