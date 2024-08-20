import random
from art import logo


def play_or_not():
    continue_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n").lower()
    if continue_or_not == "y":
        print("\n" * 10)
        print(logo)
        blackjack()


def blackjack():
    cards = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
             "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    player_hand = []
    bot_hand = []
    game_over = False

    def calculate_score(hand):
        """Take a list of card values and return the score, calculated from the cards"""
        score = sum(hand)
        if score == 21 and len(hand) == 2:
            return 0  # Blackjack
        if score > 21 and 11 in hand:
            hand.remove(11)
            hand.append(1)
        return score

    def compare(p_score, b_score):
        """Compare player and computer scores"""
        if p_score == b_score:
            return "Draw 🙃"
        elif b_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif p_score == 0:
            return "Win with a Blackjack 😎"
        elif p_score > 21:
            return "You went over. You lose 😭"
        elif b_score > 21:
            return "Opponent went over. You win 😁"
        elif p_score > b_score:
            return "You win 😃"
        else:
            return "You lose 😤"

    def draw_card():
        """Draw a random card and return its name and value"""
        card = random.choice(list(cards.items()))
        return card[0], card[1]

    # Initial two cards for player and bot
    for _ in range(2):
        player_card_name, player_card_value = draw_card()
        player_hand.append((player_card_name, player_card_value))

        bot_card_name, bot_card_value = draw_card()
        bot_hand.append((bot_card_name, bot_card_value))

    while not game_over:
        player_score = calculate_score([card[1] for card in player_hand])
        bot_score = calculate_score([card[1] for card in bot_hand])

        # Display player cards and score
        player_cards_display = ', '.join([card[0] for card in player_hand])
        print(f"Your cards: {player_cards_display}, current score: {player_score}")
        print(f"Computer's first card: {bot_hand[0][0]}")

        another_card = input("Type 'y' to get another card, type 'n' to pass:\n").lower()
        if another_card == "y":
            player_card_name, player_card_value = draw_card()
            player_hand.append((player_card_name, player_card_value))
            player_score = calculate_score([card[1] for card in player_hand])
            if player_score > 21:
                player_cards_display = ', '.join([card[0] for card in player_hand])
                print(f"Your cards: {player_cards_display}, final score: {player_score}")
                bot_cards_display = ', '.join([card[0] for card in bot_hand])
                print(f"Computer's cards: {bot_cards_display}, final score: {bot_score}")
                print(compare(player_score, bot_score))
                game_over = True
        else:
            while bot_score != 0 and bot_score < 17:
                bot_card_name, bot_card_value = draw_card()
                bot_hand.append((bot_card_name, bot_card_value))
                bot_score = calculate_score([card[1] for card in bot_hand])

            player_cards_display = ', '.join([card[0] for card in player_hand])
            bot_cards_display = ', '.join([card[0] for card in bot_hand])
            print(f"Your cards: {player_cards_display}, final score: {player_score}")
            print(f"Computer's cards: {bot_cards_display}, final score: {bot_score}")
            print(compare(player_score, bot_score))
            game_over = True

    play_or_not()


play_or_not()
