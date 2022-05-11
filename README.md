# TicTacToe-Game
- Basic Simulation of a Tic Tac Toe Game in Python

![image](https://user-images.githubusercontent.com/72391287/167771416-9edb3bc4-8adc-4be0-9e14-5774dfd0e020.png)

## Libraries used :
- OS 
- Math
- NumPy

## **Variables Used in our Project :**

- arr = Array to keep track of Player's move
- pos = Array to give Player information on the positions
- now = keeps track of which Player turn it is now i.e 1 or 2
- won = keeps track if Player1 or Player2 won 
        i.e won = 0 -> No one won
            won = 1 -> Player 1 won
            won = 2 -> Player 2 won
- first = tells us if it's the beginning of the game or not
          i.e. first = 0 -> Beginning of the Game
               first = 1 -> Not the Beginning of the Game

## **Functions to check if someone has completed a line :**

- Horizontal Check Up ->   check_horizontal() function checks for any complete horizontal line
- Vertical Check Up ->   check_vertical() function checks for complete vertical line
- Diagonal Check Up ->   check_diagonal() function checks for complete diagonal line

## **Algorithm :**

1) Refresh 3 variables for every new game i.e won, arr, first.

2) Run the Game until someone win's it i.e run the while loop until won becomes 1 or 2

3) Depending on whether it's the beginning of the game or in between :
    
  - If it's the beginning of the game i.e first = 0
    -> Ask who's going first (Player 1 or Player 2)

  - Else -> switch player's turn to ensure both player plays at alternate turns

4) Ask for the Player's move i.e row & column number -> Then mark the position with 'o' for Player1 or 'x' for Player2

5) Print the array after each move

6) Check for any complete horizontal, vertical or diagonal line

  - If found => Return the Player's no. & announce the winner --> End the loop
  - Else => Continue Playing --> Continue the loop

7) Mark first = 0 -> After the First move
