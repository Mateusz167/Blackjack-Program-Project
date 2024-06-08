# Blackjack-Program-Project

# Project Overview
This project implements a simple Blackjack game in Python. The game follows standard Blackjack rules with some specific assumptions outlined below. The project includes a main.py file with the game code and a draw.io diagram that maps out the game logic.

# Assumptions
- The deck is unlimited in size.
- There are no jokers.
- The Jack, Queen, and King all count as 10.
- The Ace can count as 11 or 1.
- Use the following list as the deck of cards: cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10].
- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer acts as the dealer.

# Files Included
- main.py: This file contains the Python code for the Blackjack game.
- art.py: This file containg art to improve user expiriance
- Blackjack_Flowchart.drawio: This file contains the draw.io diagram mapping out the game logic.

# Game Rules
- The player is dealt two cards and the dealer (computer) is dealt two cards, with one of the dealer's cards hidden.
- The player can choose to "hit" to draw additional cards or "stand" to end their turn.
- The goal is to have a hand value as close to 21 as possible without exceeding 21.
- Numbered cards count as their face value.
- Jack, Queen, and King count as 10.
- Aces can count as 11 or 1, depending on which value keeps the hand's total closer to 21 without exceeding it.
- After the player stands, the dealer reveals their hidden card and draws additional cards according to the following rules:
- The dealer must draw if their hand total is 16 or less.
- The dealer must stand if their hand total is 17 or more.
- The winner is determined by whose hand is closer to 21 without exceeding it.

# Draw.io Diagram
The diagram.drawio file contains a visual representation of the game logic, including the flow of actions and decision points. You can view and edit this diagram using the draw.io application.

# Acknowledgments
This project was inspired by the need to demonstrate coding skills in Python and understanding of basic game logic.
