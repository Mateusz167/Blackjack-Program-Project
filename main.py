from art import logo
import random

def draw_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compere_scores(player, computer):
    if player > 21 and computer > 21:
        return "You went over. You lose 😤"

    if player == computer:
        return f"Your score is {player}, computer score is {computer}. We have a draw 🙃"
    elif computer == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player == 0:
        return "Win with a Blackjack 😎"
    elif player > 21:
        return "You went over. You lose 😭"
    elif computer > 21:
        return "Opponent went over. You win 😁"
    elif player > computer:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    player_hand = []
    computer_hand = []
    is_game_over = False

    for _ in range(2):
        player_hand.append(draw_card())
        computer_hand.append(draw_card())

    while not is_game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your cards: {player_hand}, current score {player_score}")
        print(f"Computer first cards {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get next card. type 'n' to pass: ")
            if user_should_deal == 'y':
                player_hand.append(draw_card())
            else:
                is_game_over = True
    while computer_score !=0 and computer_score < 17:
        computer_hand.append(draw_card())
        computer_score = calculate_score(computer_hand)

    print(f" Your final hand {player_hand}, final score: {player_score}")
    print(f" Computer's final hand {computer_hand}, final score {computer_score}")
    print(compere_scores(player_score, computer_score))

    while input("Do you want to play Blackjack again? Type 'y' to play or 'n' to stop: ") == 'y':
        play_game()

play_game()