# Blackjack Game in Python

Welcome to the **Blackjack Game** built using Python! This game is a simple text-based implementation of the classic casino game where you compete against the dealer to reach a card sum as close to 21 as possible without going over.

## Features

- **Card Dealing**: The player and dealer receive two cards at the beginning of the game.
- **Player's Turn**: You can choose to 'Hit' (draw a card) or 'Stand' (end your turn).
- **Dealer's Turn**: The dealer follows standard rules, drawing cards until their sum is 17 or more.
- **Win Conditions**: You win if you get closer to 21 than the dealer or if the dealer goes over 21 (bust).
- **Replay Option**: After each game, you can choose to play again.

## How to Play

1. **Start the Game**: Upon running the game, you will be prompted to enter your name.
2. **Gameplay**:
   - You start with two cards, and so does the dealer (one card is hidden).
   - You can choose to "Hit" (draw a card) or "Stand" (end your turn).
   - The dealer draws cards until they reach a total of 17 or higher.
3. **Winning**: The player wins if their total is higher than the dealer's without exceeding 21, or if the dealer busts (exceeds 21).
4. **Replay**: After each round, you can choose to play again or quit.

## Setup and Installation

To run the Blackjack game on your machine:

1. **Clone this Repository**:
    ```bash
    git clone https://github.com/Avneesh-Yadav/blackjack-game.git
    ```

2. **Install Dependencies**:
    You will need Python installed on your system. This game requires the `art` module for displaying the logo.

    Install the `art` library via pip:
    ```bash
    pip install art
    ```

3. **Run the Game**:
    Navigate to the game directory and run the Python script:
    ```bash
    python blackjack.py
    ```

## Code Overview

The main game logic includes the following functions:

- **`dealer()`**: Deals initial cards to the player and dealer.
- **`player_turn()`**: Manages the player's choices during their turn (Hit or Stand).
- **`dealer_turn()`**: The dealer's logic for drawing cards until their total is 17 or more.
- **`winner_check()`**: Compares the final hands of the player and dealer to declare a winner.

## Game Flow

1. Player enters their name.
2. Cards are dealt.
3. Player makes decisions to either hit or stand.
4. Dealer draws cards based on game rules.
5. The winner is determined based on the final card sums.

## Example

### Game Start:
```
WELCOME TO BLACKJACK
Enter your name:
> John
```

### Player's Turn:
```
John's cards: [5, 9] ||| Sum: 14
Dealer's Cards: [10, *]
'1' for Hit, '2' for Stand:
> 1
```

### Game Result:
```
Your Cards: [5, 9, 7] ||| Sum: 21
Dealer's Cards: [10, 7] ||| Sum: 17
YOU WIN!!
```
